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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.annotations_operations import AnnotationsOperations
from .operations.api_keys_operations import APIKeysOperations
from .operations.export_configurations_operations import ExportConfigurationsOperations
from .operations.component_current_billing_features_operations import ComponentCurrentBillingFeaturesOperations
from .operations.component_quota_status_operations import ComponentQuotaStatusOperations
from .operations.component_feature_capabilities_operations import ComponentFeatureCapabilitiesOperations
from .operations.component_available_features_operations import ComponentAvailableFeaturesOperations
from .operations.proactive_detection_configurations_operations import ProactiveDetectionConfigurationsOperations
from .operations.components_operations import ComponentsOperations
from .operations.work_item_configurations_operations import WorkItemConfigurationsOperations
from .operations.favorites_operations import FavoritesOperations
from .operations.favorite_operations import FavoriteOperations
from .operations.web_test_locations_operations import WebTestLocationsOperations
from .operations.web_tests_operations import WebTestsOperations
from .operations.analytics_item_operations import AnalyticsItemOperations
from .operations.workbooks_operations import WorkbooksOperations
from .operations.workbook_operations import WorkbookOperations
from . import models


class ApplicationInsightsManagementClientConfiguration(AzureConfiguration):
    """Configuration for ApplicationInsightsManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ApplicationInsightsManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-applicationinsights/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ApplicationInsightsManagementClient(SDKClient):
    """Composite Swagger for Application Insights Management Client

    :ivar config: Configuration for client.
    :vartype config: ApplicationInsightsManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.applicationinsights.operations.Operations
    :ivar annotations: Annotations operations
    :vartype annotations: azure.mgmt.applicationinsights.operations.AnnotationsOperations
    :ivar api_keys: APIKeys operations
    :vartype api_keys: azure.mgmt.applicationinsights.operations.APIKeysOperations
    :ivar export_configurations: ExportConfigurations operations
    :vartype export_configurations: azure.mgmt.applicationinsights.operations.ExportConfigurationsOperations
    :ivar component_current_billing_features: ComponentCurrentBillingFeatures operations
    :vartype component_current_billing_features: azure.mgmt.applicationinsights.operations.ComponentCurrentBillingFeaturesOperations
    :ivar component_quota_status: ComponentQuotaStatus operations
    :vartype component_quota_status: azure.mgmt.applicationinsights.operations.ComponentQuotaStatusOperations
    :ivar component_feature_capabilities: ComponentFeatureCapabilities operations
    :vartype component_feature_capabilities: azure.mgmt.applicationinsights.operations.ComponentFeatureCapabilitiesOperations
    :ivar component_available_features: ComponentAvailableFeatures operations
    :vartype component_available_features: azure.mgmt.applicationinsights.operations.ComponentAvailableFeaturesOperations
    :ivar proactive_detection_configurations: ProactiveDetectionConfigurations operations
    :vartype proactive_detection_configurations: azure.mgmt.applicationinsights.operations.ProactiveDetectionConfigurationsOperations
    :ivar components: Components operations
    :vartype components: azure.mgmt.applicationinsights.operations.ComponentsOperations
    :ivar work_item_configurations: WorkItemConfigurations operations
    :vartype work_item_configurations: azure.mgmt.applicationinsights.operations.WorkItemConfigurationsOperations
    :ivar favorites: Favorites operations
    :vartype favorites: azure.mgmt.applicationinsights.operations.FavoritesOperations
    :ivar favorite: Favorite operations
    :vartype favorite: azure.mgmt.applicationinsights.operations.FavoriteOperations
    :ivar web_test_locations: WebTestLocations operations
    :vartype web_test_locations: azure.mgmt.applicationinsights.operations.WebTestLocationsOperations
    :ivar web_tests: WebTests operations
    :vartype web_tests: azure.mgmt.applicationinsights.operations.WebTestsOperations
    :ivar analytics_item: AnalyticsItem operations
    :vartype analytics_item: azure.mgmt.applicationinsights.operations.AnalyticsItemOperations
    :ivar workbooks: Workbooks operations
    :vartype workbooks: azure.mgmt.applicationinsights.operations.WorkbooksOperations
    :ivar workbook: Workbook operations
    :vartype workbook: azure.mgmt.applicationinsights.operations.WorkbookOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ApplicationInsightsManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ApplicationInsightsManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-05-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.annotations = AnnotationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.api_keys = APIKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.export_configurations = ExportConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.component_current_billing_features = ComponentCurrentBillingFeaturesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.component_quota_status = ComponentQuotaStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.component_feature_capabilities = ComponentFeatureCapabilitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.component_available_features = ComponentAvailableFeaturesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.proactive_detection_configurations = ProactiveDetectionConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.components = ComponentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.work_item_configurations = WorkItemConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.favorites = FavoritesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.favorite = FavoriteOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.web_test_locations = WebTestLocationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.web_tests = WebTestsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.analytics_item = AnalyticsItemOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workbooks = WorkbooksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workbook = WorkbookOperations(
            self._client, self.config, self._serialize, self._deserialize)
