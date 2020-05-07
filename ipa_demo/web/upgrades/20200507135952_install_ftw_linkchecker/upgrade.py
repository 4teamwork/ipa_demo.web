from ftw.upgrade import UpgradeStep


class InstallFtwLinkchecker(UpgradeStep):
    """Install ftw.linkchecker.
    """

    def __call__(self):
        self.ensure_profile_installed('profile-ftw.linkchecker:default')
        self.install_upgrade_profile()
