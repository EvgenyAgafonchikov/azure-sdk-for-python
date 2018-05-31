# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentPurgeBody(Model):
    """Describes the body of a purge request for an App Insights component.

    All required parameters must be populated in order to send to Azure.

    :param table: Required. Table from which to purge data.
    :type table: str
    :param filters: Required. The set of columns and filters (queries) to run
     over them to purge the resulting data.
    :type filters:
     list[~azure.mgmt.applicationinsights.models.ComponentPurgeBodyFilters]
    """

    _validation = {
        'table': {'required': True},
        'filters': {'required': True},
    }

    _attribute_map = {
        'table': {'key': 'table', 'type': 'str'},
        'filters': {'key': 'filters', 'type': '[ComponentPurgeBodyFilters]'},
    }

    def __init__(self, *, table: str, filters, **kwargs) -> None:
        super(ComponentPurgeBody, self).__init__(**kwargs)
        self.table = table
        self.filters = filters
