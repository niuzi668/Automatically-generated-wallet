from eth_account import Account
import json

class WalletGenerator:
    @staticmethod
    def generate_wallet():
        account = Account.create()
        return {
            "address": account.address,
            "private_key": account.key.hex()
        }

    @staticmethod
    def save_wallets(wallets, filename="wallets.json"):
        with open(filename, "w") as f:
            json.dump(wallets, f, indent=4)

if __name__ == "__main__":
    wallet_count = int(input("请输入要生成的钱包数量: "))
    wallets = [WalletGenerator.generate_wallet() for _ in range(wallet_count)]
    WalletGenerator.save_wallets(wallets)
    print(f"{wallet_count} 个钱包已生成并保存在 wallets.json 文件中。")
