# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class AvailSuppression(AWSProperty):
    """
    `AvailSuppression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, False),
        "Value": (str, False),
    }


class Bumper(AWSProperty):
    """
    `Bumper <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html>`__
    """

    props: PropsDictType = {
        "EndUrl": (str, False),
        "StartUrl": (str, False),
    }


class CdnConfiguration(AWSProperty):
    """
    `CdnConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdSegmentUrlPrefix": (str, False),
        "ContentSegmentUrlPrefix": (str, False),
    }


class DashConfigurationForPut(AWSProperty):
    """
    `DashConfigurationForPut <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfigurationforput.html>`__
    """

    props: PropsDictType = {
        "MpdLocation": (str, False),
        "OriginManifestType": (str, False),
    }


class LivePreRollConfiguration(AWSProperty):
    """
    `LivePreRollConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdDecisionServerUrl": (str, False),
        "MaxDurationSeconds": (integer, False),
    }


class AdMarkerPassthrough(AWSProperty):
    """
    `AdMarkerPassthrough <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class ManifestProcessingRules(AWSProperty):
    """
    `ManifestProcessingRules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html>`__
    """

    props: PropsDictType = {
        "AdMarkerPassthrough": (AdMarkerPassthrough, False),
    }


class PlaybackConfiguration(AWSObject):
    """
    `PlaybackConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html>`__
    """

    resource_type = "AWS::MediaTailor::PlaybackConfiguration"

    props: PropsDictType = {
        "AdDecisionServerUrl": (str, True),
        "AvailSuppression": (AvailSuppression, False),
        "Bumper": (Bumper, False),
        "CdnConfiguration": (CdnConfiguration, False),
        "ConfigurationAliases": (dict, False),
        "DashConfiguration": (DashConfigurationForPut, False),
        "LivePreRollConfiguration": (LivePreRollConfiguration, False),
        "ManifestProcessingRules": (ManifestProcessingRules, False),
        "Name": (str, True),
        "PersonalizationThresholdSeconds": (integer, False),
        "SessionInitializationEndpointPrefix": (str, False),
        "SlateAdUrl": (str, False),
        "Tags": (Tags, False),
        "TranscodeProfileName": (str, False),
        "VideoContentSourceUrl": (str, True),
    }
