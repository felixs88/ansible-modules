#!/usr/bin/python        # This is called 'shebang' or 'hashbang'

# Copyright: (c) 2021, Your Name <YourName@example.org>						# it depends on your organization
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)	# it depends on your organization


from __future__ import (absolute_import, division, print_function)	# python2 / python3 compatability issue
__metaclass__ = type							# module level declaration of metaclass



DOCUMENTATION = """
---
module: your_new_module_name

short_description: short description of your module.

description:
  - long description of your module.
  - in case multiple sentences.

version_added: "3.0.0"

options:
  option_name:
    description: option desription details
    required: True
    type: str
"""

EXAMPLES = """
---

- name: "collecting the inventory"
  namespace.collection.your_new_module_name:
    host: 127.0.0.1
    username: localhost
    password: *********
"""

RETURN = """
---
msg:
  type: str
  returned: always
  description: the output message always returned
  sample: Successfully fetched the information
error_info:
  type: dict
  returned: on error
  description: returned in case of error
  sample: error details
"""


from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec={
            "name": {"required": True, "type": "str"},
        },
        supports_check_mode=False,
    )

   # processing

   module.exit_json(msg="successfully fetched the details")


if __name__ == "__main__"
    main()

