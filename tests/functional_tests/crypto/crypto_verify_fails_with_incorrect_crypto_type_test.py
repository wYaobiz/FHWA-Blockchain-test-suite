import pytest
from indy import crypto
from utilities import common, utils
from test_scripts.functional_tests.crypto.crypto_test_base \
    import CryptoTestBase


class TestCryptoSignWithIncorrectCryptoType(CryptoTestBase):
    @pytest.mark.asyncio
    async def test(self):
        # 1. Create wallet.
        # 2. Open wallet.
        self.wallet_handle = await common.create_and_open_wallet_for_steps(
            self.steps, self.wallet_name, self.pool_name, credentials=self.wallet_credentials)

        # 3. Create verkey.
        self.steps.add_step("Create verkey")
        crypto_verkey = await utils.perform(self.steps, crypto.create_key,
                                            self.wallet_handle, "{}")

        # 4. Crypto sign the message.
        self.steps.add_step("Crypto sign the message")
        message = "Test crypto".encode()
        signature = await utils.perform(self.steps, crypto.crypto_sign,
                                        self.wallet_handle, crypto_verkey,
                                        message)

        # 5. Verify signed signature with incorrect crypto type.
        # Expected error code is 500.
        self.steps.add_step("Verify signed signature with crypto type")
        crypto_type = ":UNKNOWN_CRYPTO_TYPE"
        await utils.perform_with_expected_code(
                                        self.steps, crypto.crypto_verify,
                                        crypto_verkey + crypto_type, message,
                                        signature, expected_code=500)
