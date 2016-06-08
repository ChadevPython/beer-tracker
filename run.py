#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tracker import app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)
