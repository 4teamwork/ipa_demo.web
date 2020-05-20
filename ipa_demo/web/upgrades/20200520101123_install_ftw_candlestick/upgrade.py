from ftw.upgrade import UpgradeStep


class InstallFtwCandlestick(UpgradeStep):
    """Install ftw.candlestick.
    """

    def __call__(self):
        self.ensure_profile_installed('profile-ftw.candlestick:default')
        self.install_upgrade_profile()
