# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

from pcluster.models.imagebuilder import Build, DevSettings
from pcluster.models.imagebuilder import Image as ImageBuilderImage
from pcluster.models.imagebuilder import ImageBuilder


def dummy_imagebuilder(is_official_ami_build):
    """Generate dummy imagebuilder configuration."""
    image = ImageBuilderImage(name="Pcluster")
    if is_official_ami_build:
        build = Build(
            instance_type="c5.xlarge", parent_image="arn:aws:imagebuilder:us-east-1:aws:image/amazon-linux-2-x86/x.x.x"
        )
        dev_settings = DevSettings(update_os_and_reboot=True)
    else:
        build = Build(instance_type="g4dn.xlarge", parent_image="ami-0185634c5a8a37250")
        dev_settings = DevSettings()
    return ImageBuilder(image=image, build=build, dev_settings=dev_settings)