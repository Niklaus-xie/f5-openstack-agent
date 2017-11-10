# coding=utf-8
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""These are tests of the ESD (Enhanced Services Definition) feature.

See conftest.py for the test logic, the setup procedure, and teardown.
ESDs are defined here:

https://devcentral.f5.com/articles/customizing-openstack-lbaasv2-using-enhanced-services-definitions-25681

The esd config used by ESD_Experiment:
    f5-openstack-agent/etc/neutron/services/f5/esd/demo.json
"""
from .conftest import apply_validate_remove_validate


def test_esd_two_irules(ESD_Experiment):
    """Refactor of an historical test of a 2 irule ESD."""
    apply_validate_remove_validate(ESD_Experiment)


# Single tag tests, each individual tag is tested.
def test_esd_lbaas_ctcp(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_stcp(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_cssl_profile(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_sssl_profile(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_irule(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_policy(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_persist(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_lbaas_fallback_persist(ESD_Experiment):
    """Test a single tag."""
    apply_validate_remove_validate(ESD_Experiment)


def test_esd_full_8_tag_set(ESD_Experiment):
    """Test of a full tag set.  Tags specifics are historical."""
    apply_validate_remove_validate(ESD_Experiment)
