    "datasets": {
        "train": {
            "mode": "LRHR",
            # "dataroot_HR": "../Dataset/DIV2K/DIV2K_train_HR/result/HR_x4",
            # "dataroot_LR": "../Dataset/DIV2K/DIV2K_train_HR/result/LR_x4",
            "dataroot_HR": ".dataset/sub_HR_x4",
            "dataroot_LR": ".dataset/sub_LR_x4",
            "data_type": "npy",
            "n_workers": 2,
            "batch_size": 4,
            "LR_size": 40,
            "use_flip": true,
            "use_rot": true,
            "noise": "."
        },