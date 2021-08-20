# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Mirador 3 previewer."""

from __future__ import absolute_import, print_function

from flask import render_template

from ..proxies import current_previewer

previewable_extensions = ['tif', 'tiff', 'jpg']


def can_preview(file):
    """Check if file can be previewed."""
    return file.has_extensions('.tif', '.tiff', '.jpg')


def preview(file):
    """Preview file."""
    return render_template(
        'invenio_previewer/mirador3.html',
        file=file,
        html_tags='dir="ltr" mozdisallowselectionprint moznomarginboxes',
#        css_bundles=['pdfjs_css.css'],
        js_bundles=current_previewer.js_bundles + [
            'mirador3_js.js',
        ]
    )
