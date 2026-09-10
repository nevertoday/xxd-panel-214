<div align="center">

# XXD Panel 214｜真实固有色粗粝剪纸

把普通照片重新导演成可独立使用的艺术海报；保留主体记忆点，让材质、构图与留白共同工作。

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## 16:9 左右双联样张

以下四张为独立素材，完整 16:9 画布：左为现实摄影，右为本 Panel 设计转译，严格 50:50。文案由模型按原始提示词从当前照片智能生成。

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-05.png" alt="XXD Panel 214 样张 5"></td>
    <td width="50%"><img src="./assets/examples/sample-06.png" alt="XXD Panel 214 样张 6"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-07.png" alt="XXD Panel 214 样张 7"></td>
    <td width="50%"><img src="./assets/examples/sample-08.png" alt="XXD Panel 214 样张 8"></td>
  </tr>
</table>

## 3:4 上下双联样张

以下四张使用与 16:9 组完全不同的四张独立素材，重新生成完整 3:4 上下双联画布；上部保留现实摄影，下部遵循本 Panel 原始提示词重构。英文配字只从当前照片的内容、情绪或隐喻中生成。

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 214 新增上下样张 1"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 214 新增上下样张 2"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-11.png" alt="XXD Panel 214 新增上下样张 3"></td>
    <td width="50%"><img src="./assets/examples/sample-12.png" alt="XXD Panel 214 新增上下样张 4"></td>
  </tr>
</table>

## 适用场景与解决的问题

适合个人摄影整理、独立出版、展览练习和生活方式视觉创作。原图构图普通、背景杂乱或主体偏小，也可以通过删减、重组、裁切和尺度变化重新建立重点，而不是把照片套上滤镜。

整体呈现**极小视觉岛、大面积纯净留白、粗糙几何剪纸边、干性颗粒铺色、真实固有色与高级编辑排版**共同构成的视觉效果。远看首先感受到白纸、空间和节奏，靠近后才发现其中精巧的小图形与色彩。

## 使用窍门

- **先给一张清楚的照片：** 先选一张主体、动作和关系都容易辨认的图，再决定输出方式与比例。
- **一句话串起参数：** 直接说“上下对照 / 左右对照 / 纯设计 + 16:9 / 3:4 / 手机壁纸”，也可以补充电脑、平板或电子手表尺寸。
- **把必须保留的内容说清楚：** 指定人物、物件、动作、关系和文字；避免同时规定过多布局细节，让风格有空间完成设计。
- **文字有三种选择：** 让模型按图片智能生成、用 `--text exact --copy` 锁定逐字文案，或用 `--text none` 完全不要文字。
- **说明现实区与设计区：** 上下或左右对照时，注明哪一侧保留照片、哪一侧负责设计转译；纯设计和壁纸则说明整张画布都要重新设计。
- **先单张试，再批量做：** 先用一张图确认模式、比例、文字和语言，再把同一套参数用于目录批处理；每轮只改一个变量，结果更容易比较。

## 开始使用

从 GitHub 安装：

```bash
npx skills add https://github.com/nevertoday/xxd-panel-214 --skill xxd-panel-214
```

安装后重新启动 Agent 会话，然后调用 `$xxd-panel-214`。也可以按需追加 `--global --agent codex --yes` 做用户级安装。

常用调用示例：

```text
/xxd-panel-214 photo.jpg --mode top-bottom --size 3:4 --text prompt --locale zh-CN
/xxd-panel-214 photo.jpg --mode left-right --size 16:9 --text prompt --locale en-US
/xxd-panel-214 photo.jpg --mode design-only --size 9:16 --text none --prefs off
/xxd-panel-214 ./photos --mode design-only --size auto,3:4 --text prompt --locale ja-JP
```

完整运行契约见 [SKILL.md](SKILL.md)；运行适配器见 [英文](references/xxd-panel-214-prompt.en.md) 与 [中文](references/xxd-panel-214-prompt.zh-CN.md)。

## 原始提示词

[中文完整原稿](references/original-prompt/zh-CN.md)逐字保留，是运行时唯一的创作与审美权威。本批提供五语使用说明，不另做四份长原稿译文；风格简介只用于检索，不得替代原文。

## 快速判断：Panel 214 适合你吗？

既要保留源图身份，也要重新构图；既要材质特征，也要主动留白。可选准确文字、智能文案或无文字；支持单图、递归目录批量以及下方四种交付模式。

## 四种输出模式

- `top-bottom`：整张画布只有上下两个全宽区域，现实照片在上、设计在下，严格各占 50%。
- `left-right`：整张画布只有左右两个全高区域，现实照片在左、设计在右，严格各占 50%，不会旋转成上下结构。
- `design-only`：整张画布只呈现 Panel 214 的设计转译，照片只作为不可见参考。
- `wallpaper-pack`：按手机、iPad、桌面和手表分别生成完整设计壁纸，可选 `linked` 连贯套装或 `independent` 四张独立。

支持多选模式与比例（`1:1`、`3:4`、`4:3`、`4:5`、`5:4`、`2:3`、`3:2`、`9:16`、`16:9`、`21:9`、`5:7`、`7:5` 或准确像素），以及模型生成文字、准确文字和无文字。传入目录会递归扫描图片，每张源图独立处理，共用一次交付设置；最终 PNG 平铺放入一个新任务目录。

<!-- xxd-readme-ads:start -->
## 关于 XXD

XXD 是小小东品牌名的缩写，本项目由小小东创建并维护：[@xiaoxiaodong01](https://x.com/xiaoxiaodong01)。

## 小小东多端会员 · 699 元/年

> **广告与商业信息声明：** 以下二维码、会员与付费服务链接属于小小东的广告信息。是否扫码或购买完全自愿，不影响本开源项目的访问与使用。

一次年费，同时开通三项会员权益：**知识星球 + 小小东成员提示词库 + 全部 将军总指挥 Skills 会员**。三项权益合并在同一份会员中，无需分别购买。

<!-- xxd-panel-command-system:start -->

### Skills 如何协作

| 层级 | 包含内容 | 用途 |
|---|---|---|
| **General** | [`xxd-panel-all`](https://github.com/xiaoxiaodong-ai/xxd-panel-all) | 识别可用的编号 Skills，按图片、主题和用途推荐，并组织多风格试稿与批量任务。 |
| **Soldier** | `xxd-panel-NNN` | 每个编号执行自己的原始提示词与审美，完成 General 分派的具体任务。 |

<!-- xxd-panel-command-system:end -->

### 会员权益

1. **微信一对一 AI 学习与项目答疑**
   扫描下方二维码，添加小小东微信，围绕 AI 学习、工具使用和实际项目进行一对一沟通，获得答疑与建议；代表性问题将整理为会员内容。
2. **持续更新的成员提示词库**
   [小小东成员提示词库](https://vip.xiaoxiaodong.ai/)当前约有 3.2 万条提示词，会持续整理和扩充，目标超过 10 万条。
3. **全部 将军总指挥 Skills 与使用答疑**
   一份会员覆盖全部 将军总指挥 Skills；使用过程中遇到问题，可以获得相应的使用说明与答疑。
4. **高频刚需优先处理**
   会员提出的高频、刚需提示词与 Skills 需求，会优先评估和开发。

### 如何开通

- 可在[成员网站](https://vip.xiaoxiaodong.ai/)自助开通。
- 也可以扫描下方二维码，添加小小东微信，进行一对一沟通并获得开通协助。

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="联系小小东" width="280"></a></p>
<!-- xxd-readme-ads:end -->

## 许可证

本项目（包括 Skill、提示词、脚本、文档及随附样张）采用 **PolyForm Noncommercial License 1.0.0**。完整法律条文请见 [LICENSE](LICENSE)，官方页面见 <https://polyformproject.org/licenses/noncommercial/1.0.0>。

许可范围说明：

- 个人可以用于学习、研究、实验、测试、兴趣项目和私人娱乐；慈善机构、教育机构、公共研究/安全/卫生机构、环保组织及政府机构也可以使用。
- 在**非商业目的**下，你可以使用、复制、修改、制作衍生作品并分享；分享时必须同时提供本许可证（或上面的链接）以及作者提供的所有 `Required Notice:` 声明。
- 不允许用于商业产品或服务、收费交付、出售访问权或许可，或任何预期会带来商业应用的用途。需要商业使用时，请先向版权方另行取得书面许可。
- 本协议只授予其中明确写出的著作权许可和有限的专利许可，不授予商标、品牌名称或其他未明确授予的权利，也不能把你的许可再转授给他人。
- 如果收到书面违约通知，须在 32 天内纠正并采取实际补救措施，否则许可会立即终止；就专利侵权提出书面主张也会终止专利许可。
- 内容按“现状”提供，在法律允许的范围内不作任何担保，使用风险和可能的损失由使用者自行承担。
