# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

no_cache = 1
import frappe
from aetesis.e_commerce.shopping_cart.cart import get_cart_quotation


def get_context(context):
	context.body_class = "product-page"
	quotation = get_cart_quotation()
	
	context.update(quotation)
