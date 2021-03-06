from utilities import utils
from utilities import common, constant
from test_scripts.functional_tests.pool.pool_test_base import PoolTestBase
import pytest


class TestCreatePoolLedgerConfig(PoolTestBase):

    @pytest.mark.asyncio
    async def test(self):
        # 1. Create a pool ledger config.
        self.steps.add_step("Create pool ledger config")
        result = await \
            utils.perform(self.steps, common.create_pool_ledger_config,
                          self.pool_name, constant.pool_genesis_txn_file,
                          ignore_exception=True)
        # 2. Verify that pool ledger config is created.
        self.steps.add_step("Verify that pool ledger config is created")
        error_message = "Cannot create a pool ledger config"
        utils.check(self.steps, error_message,
                    condition=lambda: not isinstance(result, Exception) and
                    utils.check_pool_exist(self.pool_name))
