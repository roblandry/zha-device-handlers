from zigpy.profiles import PROFILES, zha
from zigpy.zcl.clusters.general import Basic, Identify, Groups,\
    Scenes, OnOff, Ota
from zigpy.zcl.clusters.homeautomation import ElectricalMeasurement
from quirks import EventableCluster
from zigpy.quirks import CustomDevice


DIAGNOSTICS_CLUSTER_ID = 0x0B05  # decimal = 2821


class CentraLite4257050RZHAC(CustomDevice):

    class EventableOnOffCluster(EventableCluster, OnOff):
        cluster_id = OnOff.cluster_id

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    signature = {
        #  <SimpleDescriptor endpoint=1 profile=260 device_type=256
        #  device_version=0
        #  input_clusters=[0, 3, 4, 5, 6, 2820, 2821]
        #  output_clusters=[25]>
        1: {
            'profile_id': zha.PROFILE_ID,
            'device_type': zha.DeviceType.ON_OFF_SWITCH,
            'input_clusters': [
                Basic.cluster_id,
                Identify.cluster_id,
                Groups.cluster_id,
                Scenes.cluster_id,
                #OnOff.cluster_id,
                ElectricalMeasurement.cluster_id,
                DIAGNOSTICS_CLUSTER_ID
            ],
            'output_clusters': [
                Ota.cluster_id
            ],
        },
    }

    replacement = {
        'manufacturer': 'CentraLite',
        'model': '4257050-RZHAC',
        'endpoints': {
            1: {
                'input_clusters': [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    ElectricalMeasurement.cluster_id,
                    DIAGNOSTICS_CLUSTER_ID
                ],
                'output_clusters': [
                    EventableOnOffCluster,
                    Ota.cluster_id
                ],
            }
        },
    }
