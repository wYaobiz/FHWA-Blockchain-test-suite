import pytest
import json

from indy import did
from utilities import common, constant
from utilities import utils
from test_scripts.functional_tests.did.signus_test_base \
    import DidTestBase


class TestCreateDidWithPassedDid(DidTestBase):
    @pytest.mark.asyncio
    async def test(self):
        # 1. Create wallet.
        # 2. Open wallet.
        self.wallet_handle = await \
            common.create_and_open_wallet_for_steps(self.steps,
                                                    self.wallet_name,
                                                    self.pool_name,
                                                    credentials=self.wallet_credentials)

        # 3. Create did and verkey with passed did.
        self.steps.add_step("Create did and verkey with passed did")
        did_json = json.dumps({"did": constant.did_my1})
        (my_did, _) = await \
            utils.perform(self.steps, did.create_and_store_my_did,
                          self.wallet_handle, did_json)

        # 4. Check created did.
        self.steps.add_step("Check created did")
        utils.check(self.steps, error_message="Created did is invalid",
                    condition=lambda: my_did == constant.did_my1)
