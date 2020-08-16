from rest_framework import serializers
from list_org_parser.models import OrganizationUrl


class OrganizationUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationUrl
        fields = ['urls', 'is_active', 'create_date']
