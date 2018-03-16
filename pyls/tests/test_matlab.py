# -*- coding: utf-8 -*-

import os.path as op
import pkg_resources
import pyls

data_dir = pkg_resources.resource_filename('pyls', 'tests/data')
EXAMPLES = ['mpls_multigroup_onecond_nosplit.mat',
            'mpls_multigroup_onecond_split.mat',
            'bpls_onegroup_onecond_nosplit.mat',
            'bpls_onegroup_onecond_split.mat']

attrs = ['u', 's', 'v', 'usc', 'vsc', 'perm_result', 'boot_result', 'inputs']


def test_import_matlab():
    for fname in EXAMPLES:
        res = pyls.matlab.import_matlab_result(op.join(data_dir, fname))
        # make sure the mat file cast appropriately
        assert isinstance(res, pyls.base.PLSResults)
        # make sure all the attributes are there (don't check outputs)
        for attr in attrs:
            assert hasattr(res, attr)
        if '_split' in fname:
            assert hasattr(res, 'perm_splithalf')
