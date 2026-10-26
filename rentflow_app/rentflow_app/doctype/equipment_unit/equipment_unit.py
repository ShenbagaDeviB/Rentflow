# Copyright (c) 2026, Shenbaga Devi and contributors
# For license information, please see license.txt

import frappe  # type: ignore[reportMissingImports]
from frappe.model.document import Document  # type: ignore[reportMissingImports]


class EquipmentUnit(Document):
	def autoname(self):
		self.name = frappe.model.naming.make_autoname(
			f"{self.category[:3].upper()}-.#####"
		)
