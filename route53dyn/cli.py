# -*- coding: utf-8 -*-
"""Console script for route53dyn"""
import datetime
import sys
from typing import Optional
import time

import click
import json
from click.testing import CliRunner
import boto3
import requests

last_external_ip: Optional[str] = None

route53_client = boto3.client('route53')


class DatetimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(DatetimeEncoder, self).default(obj)


def is_debugging():
    return not (sys.gettrace() is None)


def log(result):
    click.echo(json.dumps(result, indent=2, cls=DatetimeEncoder))


def get_hosted_zone_id(dns_name: str):
    return route53_client.list_hosted_zones_by_name(DNSName=dns_name)['HostedZones'][0]['Id']


def get_external_ip():
    return requests.get('https://api.ipify.org').text


def update_dns_record(dns_name: str, ip_address: str, names: []):
    zone_id = get_hosted_zone_id(dns_name)

    changes = []
    for name in names:
        change = {
            'Action': 'UPSERT',
            'ResourceRecordSet': {
                'Name': name,
                'Type': 'A',
                'TTL': 180,
                'ResourceRecords': [
                    {
                        'Value': ip_address
                    },
                ],
            }
        }

        changes.append(change)

    response = route53_client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Comment': 'Automatic DNS update',
            'Changes': changes
        }
    )
    return response


def monitor(dns_name, host_names):
    global last_external_ip
    while True:
        current_external_ip = get_external_ip()

        click.echo(f'Checking if current {current_external_ip} ip address differs from last '
                   f'known ip address ({last_external_ip})')

        if last_external_ip != current_external_ip:
            last_external_ip = current_external_ip
            log(update_dns_record(dns_name, current_external_ip, host_names))
        time.sleep(10)


@click.command()
@click.argument('dns_name', envvar='ROUTE53DYN_DNS_NAME')
@click.argument('host_names', envvar='ROUTE53DYN_HOST_NAMES')
def main(dns_name, host_names: str):
    """Console script for awsify."""
    host_names_list = [x.strip() for x in host_names.split(',')] or [host_names]
    monitor(dns_name, host_names_list)


if __name__ == "__main__":
    if is_debugging():
        runner = CliRunner()
        runner.invoke(main)
    else:
        main()
