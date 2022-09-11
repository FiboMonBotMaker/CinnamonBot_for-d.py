import discord
from discord import Interaction, SelectOption, app_commands
from discord.ext import commands
from discord.ui import *


class ListView(View):
    def __init__(self):
        super().__init__(timeout=30)
        self.add_item(CommandList())

class CommandList(Select):
    def __init__(self):
        options = []
        options.append(SelectOption(label="メインコマンド", emoji="📰", description="メインコマンドです。たくさんのコマンド（ほぼネタ）があります。"))
        options.append(SelectOption(label="謎物語生成コマンド", emoji="📚", description="謎の物語を生成するコマンドです。使えば使うほどカオスになっていくコマンドです。"))
        options.append(SelectOption(label="いつどこ生成コマンド", emoji="🛰", description="いつどこゲームができるコマンドです。ランダムで謎の文章を作れます。"))
        options.append(SelectOption(label="お金関連コマンド", emoji="💰", description="いつどこゲームができるコマンドです。ランダムで謎の文章を作れます。"))
        options.append(SelectOption(label="みんはやコマンド", emoji="💬", description="早押しクイズができるコマンドです。正解するとお金を稼げます。"))
        options.append(SelectOption(label="スパチャコマンド", emoji="💎", description="Youtubeのアレなコマンドです。お金を送りあえます。"))
        options.append(SelectOption(label="todoコマンド", emoji="📝", description="todoができるコマンドです。積極的に活用してみましょう。"))
        options.append(SelectOption(label="nbコマンド", emoji="🗯", description="nbさんの名言を出すコマンドです。たくさんの、コマンドが、あるんだねぇ。"))
        options.append(SelectOption(label="競馬コマンド", emoji="🗯", description="お金をかけて競馬するコマンドです。ハマりすぎには気をつけてください。"))
        options.append(SelectOption(label="Statコマンド", emoji="📇", description="マイクラ鯖の情報を取得するやつです。"))

        super().__init__(placeholder="表示するヘルプコマンドを指定してね", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: Interaction):
        embed = discord.Embed(title=f"helpコマンド：{self.values[0]}",color=0x1e90ff)
        if self.values[0] == "メインコマンド":
            print("main")
            embed.add_field(
                name=f"どのジャンルにも属さない、適当なコマンドたちです。便利コマンドからネタコマンドまで、適当に作ったコマンドを放り込んだやつたちです。",
                value=f"\
                    \n**・/etc hello**\nテスト用だったコマンドです。あいさつをしてくれるよ！\
                    \n**・/etc mention**\nしなもんにメンションするコマンドです。私に爆撃したいときにどうぞ！（ほどほどに）\
                    \n**・/etc face**\nマイクラスキンを取得して顔写真を生成するコマンドです！\
                    \n**・/etc seichi**\nしなもんに整地させるコマンドです。整地鯖の投票リンクなどもあります！\
                    \n**・/etc code**\n文章をコードにするコマンドです。改行コードが使えますよ！\
                    \n**・/etc github**\n主に開発者用コマンドです。このbotのコードがのってます！\
                    \n**・/etc reference**\n主に開発者用コマンドです。Pycodeむずい！たのしい！\
                    \n**・/etc 5000oku**\n5000兆円欲しいコマンドです。コマンド名は間違えて億になってますね。直す気はありません"
                )
        elif self.values[0] == "謎物語生成コマンド":
            print("uioj")
            embed.add_field(
                name=f"昔にあったふぃぼなっちさんのbotの機能を模倣したものです。使う人は少ないですが、たまにやると神回が登場して面白い気がします。",
                value=f"\
                    \n**・/story get**\n謎の物語を表示するコマンドです。鯖民が一文ずつ寄せ合わせでてきたカオスな文章だよ！\
                    \n**・/story shuffle**\n謎の物語をシャッフルして表示するコマンドです。カオスな文章がさらにカオスになってくるよ！\
                    \n**・/story set**\n謎の物語に文章を追加するコマンドです。君も意味不明な文を追加してカオスにしてみよう！\
                    \n**・/story remove**\n追加した文章を削除するコマンドです。誤字ったものを追加しちゃったりしたとき用です！\
                    \n**・/story trans**\nシャッフルした物語を再翻訳するコマンドです。ガチで意味不明すぎておなか痛くなるので注意！\
                    "
                )
        elif self.values[0] == "いつどこ生成コマンド":
            print("uioj")
            embed.add_field(
                name=f"このbot制作のきっかけのコマンドです。暇つぶし用に作ったもので、このコマンドでbot制作の基礎が学べた気がします。",
                value=f"\
                    \n**・/itudoko get**\nいつどこゲームを表示コマンドです。実行するだけでも結構面白い！\
                    \n**・/itudoko set**\nいつどこゲームに単語を追加するコマンドです。なにか思いついたら追加してみよう！\
                    \n**・/itudoko trans**\nいつどこゲームの結果を再翻訳するコマンドです。たまに神回ができるので面白いよ！\
                    "
                )
        elif self.values[0] == "お金関連コマンド":
            print("main")
            embed.add_field(
                name=f"最初は何かやりこみ要素を追加したいと思って追加した機能です。せっかくできた機能なので活用する場面を増やしていきたいですね...",
                value=f"\
                    \n**・/money check**\n所持金を確認するコマンドです。金持ちをめざそう！\
                    \n**・/money down**\n所持金を減らすコマンドです。私以外使う人はいないと思う...\
                    \n**・/money genshin**\nキャラ名から原神のガチャ絵を取得するコマンドです。もとはガチャのキャラ絵表示のためにテスト用で作ったもの。\
                    \n**・/money genshinwish**\n原神のガチャを引くコマンドです。演出も含めて作成にかなり頑張りました。ぜひやってみてね！\
                    \n**・/money genshinwish_n**\n原神のガチャをたくさん引くコマンドです。200連くらいできるので豪遊気分を味わいたい方はぜひ！\
                    "
                )
        elif self.values[0] == "みんはやコマンド":
            print("uioj")
            embed.add_field(
                name=f"四択なので鯖民で競い合ってどうぞ。謎にスプラとか専門用語が誕生したり、けっこうガチ界隈になってる模様。ボタンの実装が結構大変でトラウマになりました。",
                value=f"\
                    \n**・/hayaoshi get**\n問題をランダムで表示するコマンドです。正解したらお金も稼げるよ！\
                    \n**・/hayaoshi add**\n問題を追加するコマンドです。問題を追加してもお礼にお金がもらえるよ！よりよい問題制作を心掛けてね。\
                    "
                )
        elif self.values[0] == "スパチャコマンド":
            print("main")
            embed.add_field(
                name=f"昔に存在した旧しなもんbotからの移植です。みかんさんの協力もあって、旧botより格段にきれいに、使いやすくなりました。歴史あるコマンドです（？）",
                value=f"\
                    \n**・/superchat give**\nスパチャを送信するコマンドです。相手を指定して送金することもできるよ！\
                    \n**・/superchat set**\nスパチャする前に、アイコンとかをセットアップするコマンドです。口座開設的な？アカウント作成的な？\
                    "
                )
        elif self.values[0] == "todoコマンド":
            print("main")
            embed.add_field(
                name=f"これも昔にあったふぃぼなっちさんのbotの模倣です。bot開発が進んでいく中で、todoリストがあったら便利だと思って作ってもらいました（ありがとうみかんさん）。やっぱtodoはいいね。慣れたら便利です。",
                value=f"\
                    \n**・/todo check**\ntodoを確認するコマンドです。\
                    \n**・/todo add**\ntodoを追加するコマンドです。やりたいと思ったことはすぐtodoに追加すると忘れないから便利だよ！\
                    \n**・/todo remove**\ntodoから特定のtodoを削除するコマンドです。間違えて追加してたり、todoの内容を達成したときに！\
                    "
                )
        elif self.values[0] == "nbコマンド":
            print("uioj")
            embed.add_field(
                name=f"nbさんの名言が詰まったコマンドジャンルです。制作者：nikawamikanさん。",
                value=f"\
                    \n**・/nb home**\n褒められたときに使えるコマンドです。\
                    \n**・/nb youtube**\nnbさんの名言に単語を当てはめて生成できるっぽいです。\
                    \n**・/nb meigen**\nnbさんの名言をランダムで出してくれるっぽいです。\
                    "
                )
        elif self.values[0] == "いつどこ生成コマンド":
            print("uioj")
            embed.add_field(
                name=f"所持金をかけて競馬をコマンドです。一着でかなりのお金がもらえます。FirestormMino作。",
                value=f"\
                    \n**・/keiba register**\n競馬できるコマンドです。目指せ一攫千金！\
                   ")
        elif self.values[0] == "Statコマンド":
            print("uioj")
            embed.add_field(
                name=f"昔作ったコマンドのリメイク版。めっちゃ見やすくなったしめっちゃ機能的になりました。成長を感じたコマンドです。",
                value=f"\
                    \n**・/stat get**\n情報を取得するコマンドです。今参加してるメンバーとかを確認できるよ！\
                    \n**・/stat set**\n鯖のurlを設定するコマンドです。何らかの要因でurlが変わったときに使おう。\
                   ")
        await interaction.response.edit_message(embed=embed, view=ListView())

class SendList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="chelp", description="しなもんbotに困ったらまずはこれ！")
    async def help(self, interaction: Interaction):
        await interaction.response.send_message("確認したいコマンドのジャンルを選択してね", view=ListView())

async def setup(bot):
    await bot.add_cog(SendList(bot))
