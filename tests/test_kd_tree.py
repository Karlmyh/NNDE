from ..NNDE._kd_tree import KDTree import numpy as npDIM = 10NTRAIN = 200NTEST = 200def test_kd_tree_query():            X_train = np.random.rand(DIM*NTRAIN).reshape(-1,DIM)    X_test = np.random.rand(DIM*NTEST).reshape(-1,DIM)        tree = KDTree(X_train)                  dist, ind = tree.query(X_test, k=3)      assert dist.shape == (NTEST , 3)    assert ind.shape == (NTEST , 3)        def test_kd_tree_adaptive_query():            X_train = np.random.rand(DIM*NTRAIN).reshape(-1,DIM)    X_test = np.random.rand(DIM*NTEST).reshape(-1,DIM)        tree = KDTree(X_train)                  dist, k = tree.adaptive_query(X_test, C=10)      assert dist.shape == (NTEST , )    assert k.shape == (NTEST , )