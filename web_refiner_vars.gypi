# Copyright (c) 2015-2016 Qualcomm Technologies, Inc.
# All Rights Reserved.
# Confidential and Proprietary - Qualcomm Technologies, Inc.

{
  'variables': {
    'web_refiner_native_libs%' : [
      '<(SHARED_LIB_DIR)/libswewebrefiner.so',
    ],
    'web_refiner_dependencies%' : [
      '<(DEPTH)/components/web_refiner/web_refiner.gyp:web_refiner_native',
      '<(DEPTH)/components/web_refiner/web_refiner.gyp:web_refiner_java',
    ],
  },
}
