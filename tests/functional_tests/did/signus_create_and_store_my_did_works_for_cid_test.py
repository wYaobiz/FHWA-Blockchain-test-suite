import pytest
import json

from indy import did
from utilities import common, constant
from utilities import utils
from test_scripts.functional_tests.did.signus_test_base \
    import DidTestBase


class TestCreateDidWithCid(DidTestBase):
    @pytest.mark.asyncio
    async def test(self):
        # 1. Create wallet.
        # 2. Open wallet.
        self.wallet_handle = await \
            common.create_and_open_wallet_for_steps(self.steps,
                                                    self.wallet_name,
                                                    self.pool_name,
                                                    credentials=self.wallet_credentials)

        # 3. Create did and verkey with cid.
        self.steps.add_step("Create did and verkey with cid")
        (my_did, my_verkey) = await \
            utils.perform(self.steps,
                          did.create_and_store_my_did, self.wallet_handle,
                          json.dumps({"seed": constant.seed_my1, "cid": True}))

        # 4. Check created did.
        self.steps.add_step("Check created did")
        utils.check(self.steps, error_message="Created did is invalid",
                    condition=lambda: my_did == constant.verkey_my1)

        # 5. Check created verkey.
        self.steps.add_step("Check created verkey")
        utils.check(self.steps, error_message="Created verkey is invalid",
                    condition=lambda: my_verkey == constant.verkey_my1)
