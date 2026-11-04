# Prose Polish — Biên Bản Sai Lệch, Arc 1 hiện có

> Cập nhật 04/11/2026: đã apply cả 20 preview theo lời duyệt trực tiếp. Xem [APPLY_REPORT.md](APPLY_REPORT.md). Nội dung dưới đây lưu báo cáo tại thời điểm preview, gồm cổng duyệt khi ấy.

Ngày: 04/11/2026. Branch: `edit/bien-ban-sai-lech-prose-polish-arc1`.
Baseline: `239af1d` (HEAD sạch về nội dung dự án khi bắt đầu; `.serena/` chưa được theo dõi đã có sẵn, được giữ nguyên).

## Kết quả và bản đọc

**20/20 chương đã được biên tập thành preview, chưa apply vào bản chính thức.** Chỉ chương 001–020 tồn tại; dàn ý30 chương không có nghĩa Arc1 đã hoàn tất. Không tạo021, không lập Arc2.

- [Đọc liền toàn bộ20 preview](PREVIEW_ALL.md).
- [Mục lục từng chương và ghi chú](README.md).
- [So sánh đầy đủ mọi đoạn thay đổi](FULL_COMPARISON.diff).
- [Bảng số từ, đoạn, SHA preview](word-counts.csv).
- [Style Guide đề xuất](../../STYLE_GUIDE.md).
- [Review toàn tuyến](ARC_REVIEW.md); review từng batch nằm cạnh báo cáo này.

Mỗi preview có snapshot nguồn, snapshot approval, manifest, review gắn SHA và báo cáo helper trong `.novel/prose-polish/arc1-batch1` đến `arc1-batch4`. Tất cả session giữ `applied=false`.

## Những cải thiện chính

Các câu kể cùng một điểm chú ý được nối để hành động, quan sát và phản ứng liền nhau. Giảm nhịp liệt kê quanh sổ, máy, ảnh và bàn giao; làm rõ chủ thể khi đổi người cầm vật. Những đoạn vốn đã tự nhiên được giữ lại. Không sửa hội thoại chỉ để tạo dấu vết biên tập.

Nhịp ngắn vẫn giữ ở đếm bậc, lệnh dừng, tiếng đáp, phát hiện T12, bốn nhịp kéo và những lựa chọn khó. Không thêm chi tiết cảm giác, động cơ hay bí mật để làm đẹp câu. Không kéo cảnh căng bằng chuỗi câu dài; nét hài khô của Khải, Lam, Duy và Phúc còn nguyên. Cảnh bà Năm giữ lời nói và vật bà chọn đưa ra, không thêm diễn giải thương cảm.

Tổng cộng148 khối khác biệt theo đối chiếu dòng; đây là mô tả phạm vi, không là thước đo chất lượng. Bốn lượt biên tập ban đầu có150 cặp thay thế; một số nằm liền nhau nên được tính chung trong diff.

## 10 ví dụ trước/sau thực tế

Các trích đoạn dưới đây được lấy trực tiếp từ source và preview cuối, không dựng ví dụ minh họa. Full diff giữ cả những đoạn không được trích ở đây.

### 1. Chương001

**Trước:**

> Anh đợi cô giải thích thêm. Hạ Lam không nói. Cô đang nhìn màn hình thiết bị ghi hình gắn trước ngực; đèn đỏ nhỏ vẫn nhấp nháy đều.

**Sau:**

> Anh đợi cô giải thích thêm, nhưng Hạ Lam không nói. Mắt cô dừng ở màn hình thiết bị ghi hình gắn trước ngực, nơi đèn đỏ nhỏ vẫn nhấp nháy đều.

### 2. Chương002

**Trước:**

> Anh chưa định bước, nhưng mũi giày đã quay về phía tiếng người. Chính anh cũng chỉ nhận ra khi nhìn xuống. Mẩu băng giấy ghi số một nằm cách chân chưa đầy nửa mét. Xa hơn, những con số chì anh viết nối vào bóng tối.

**Sau:**

> Anh chưa định bước, vậy mà khi nhìn xuống mới nhận ra mũi giày đã quay về phía tiếng người. Mẩu băng giấy ghi số một nằm cách chân chưa đầy nửa mét. Xa hơn, những con số chì anh viết nối vào bóng tối.

### 3. Chương004

**Trước:**

> Khải đứng thẳng dậy. Cột sống anh nhói lên vì cúi quá lâu. Đầu anh vẫn tự nối hai mảnh hình: từ bậc hai mươi hai tới cửa bảy, đúng một vế mười một bậc. Nếu chỉ nhìn video, người xem có thể nghĩ anh đi nốt đoạn ngắn rồi quay lại. Nếu chỉ nghe hai người kể, người ta có thể hỏi tại sao họ không đếm nhầm.

**Sau:**

> Khải đứng thẳng dậy, cột sống nhói lên vì cúi quá lâu, còn trong đầu vẫn tự nối hai mảnh hình: từ bậc hai mươi hai tới cửa bảy, đúng một vế mười một bậc. Nếu chỉ nhìn video, người xem có thể nghĩ anh đi nốt đoạn ngắn rồi quay lại. Nếu chỉ nghe hai người kể, người ta có thể hỏi tại sao họ không đếm nhầm.

### 4. Chương005

**Trước:**

> Khải đặt điện thoại lên miếng bìa. Sơ đồ cũ có màu vàng xám của giấy qua lớp nhựa; bản mới sáng trắng, ký hiệu đỏ và xanh sắc cạnh. Anh phóng lớn cùng một khu vực ở mỗi ảnh, chụp lại phần màn hình để có thể chuyển qua lại mà không mất chỗ. Đó là hai ảnh anh tự làm thêm, anh để chúng đứng sau ảnh gốc, không thay thế chúng.

**Sau:**

> Khải đặt điện thoại lên miếng bìa. Sơ đồ cũ có màu vàng xám của giấy qua lớp nhựa; bản mới sáng trắng, ký hiệu đỏ và xanh sắc cạnh. Anh phóng lớn cùng một khu vực ở mỗi ảnh rồi chụp màn hình, để lúc chuyển qua lại không mất chỗ. Hai ảnh làm thêm được xếp sau ảnh gốc, giữ riêng với chúng.

### 5. Chương006

**Trước:**

> Âm thanh rất nhỏ, giống có người kéo móng tay dọc một cái lon. Anh ngừng viết, giữ nguyên cổ tay trên mép bìa. Bên cạnh, Thu cũng ngẩng đầu. Bàn tay chị vẫn đè trên góc bản phác. Duy đang cuộn dây nguồn máy tính; cậu buông vòng dây xuống đầu gối để nghe.

**Sau:**

> Âm thanh rất nhỏ, giống có người kéo móng tay dọc một cái lon. Anh ngừng viết, cổ tay giữ nguyên trên mép bìa. Bên cạnh, Thu cũng ngẩng đầu, bàn tay vẫn đè trên góc bản phác. Duy đang cuộn dây nguồn máy tính; cậu buông vòng dây xuống đầu gối để nghe.

### 6. Chương007

**Trước:**

> Khải đang vặn nắp chai nước. Anh nhìn bàn tay ông, chờ tiếng kim loại dừng hẳn mới hỏi:

**Sau:**

> Đang vặn nắp chai nước, Khải nhìn bàn tay ông, chờ tiếng kim loại dừng hẳn mới hỏi:

### 7. Chương010

**Trước:**

> Khải cúi một chút. Cổ áo cọ vào phần gáy khô mồ hôi khiến anh rùng mình. Anh đã rửa mặt và uống nước ở sảnh, nhưng mí mắt vẫn nặng, mỗi lần chớp có cảm giác như hai bề mặt ráp kéo qua nhau. Anh đưa đèn của mình cho Lam thay vì cố cầm hai thứ một lúc.

**Sau:**

> Khải hơi cúi xuống, rùng mình khi cổ áo cọ vào phần gáy khô mồ hôi. Anh đã rửa mặt và uống nước ở sảnh, nhưng mí mắt vẫn nặng, mỗi lần chớp có cảm giác như hai bề mặt ráp kéo qua nhau. Anh đưa đèn của mình cho Lam thay vì cố cầm hai thứ một lúc.

### 8. Chương012

**Trước:**

> Thu đứng dậy ở phía sau. Chiếc ghế kéo trên nền phát tiếng ken két.

**Sau:**

> Phía sau, Thu đứng dậy, chiếc ghế kéo trên nền ken két.

### 9. Chương017

**Trước:**

> Ông Phúc kéo ghế ra sau. Tiếng chân ghế làm Thu ngẩng lên. Ông không đứng dậy, chỉ rời mép bàn một quãng đủ để không ai đưa giấy tới trước ngực mình.

**Sau:**

> Ông Phúc kéo ghế ra sau, tiếng chân ghế khiến Thu ngẩng lên. Ông vẫn ngồi, cách mép bàn một quãng đủ để không ai đưa giấy tới trước ngực mình.

### 10. Chương020

**Trước:**

> Anh không tẩy nét ấy. Anh dùng tờ khác vẽ riêng chỗ đứng và hướng quan sát, rồi để hai bản cạnh nhau cho người nhận thấy vì sao phải đổi. Chỉ vài phút trước anh còn thấy công việc này là thứ ngăn mình tới kho. Đến mũi tên thứ ba, anh hiểu nó có thể ngăn một người khác đi sai trong lúc mình vắng mặt.

**Sau:**

> Anh giữ nguyên nét ấy, dùng tờ khác vẽ riêng chỗ đứng và hướng quan sát rồi đặt hai bản cạnh nhau, cho người nhận thấy vì sao phải đổi. Chỉ vài phút trước anh còn thấy công việc này là thứ ngăn mình tới kho. Đến mũi tên thứ ba, anh hiểu nó có thể ngăn một người khác đi sai trong lúc mình vắng mặt.

## Số từ và đoạn theo chương

Đếm bằng whitespace split, gồm tiêu đề, giống helper và QA dự án. Với tiếng Việt, đây là đơn vị cách nhau bằng khoảng trắng, không phải bộ tách từ ngôn ngữ học. Không dùng số từ hoặc độ dài câu trung bình để chấm văn chương.

| Chương | Trước | Sau | Chênh | Đoạn trước → sau |
|---|---:|---:|---:|---:|
| 001 | 3066 | 3069 | +3 | 144 → 141 |
| 002 | 1986 | 1983 | -3 | 65 → 65 |
| 003 | 1900 | 1899 | -1 | 58 → 58 |
| 004 | 1937 | 1939 | +2 | 53 → 53 |
| 005 | 1958 | 1946 | -12 | 40 → 40 |
| 006 | 2295 | 2296 | +1 | 78 → 78 |
| 007 | 2331 | 2330 | -1 | 99 → 99 |
| 008 | 2174 | 2173 | -1 | 43 → 43 |
| 009 | 2168 | 2166 | -2 | 75 → 75 |
| 010 | 2204 | 2207 | +3 | 58 → 58 |
| 011 | 1987 | 1985 | -2 | 48 → 48 |
| 012 | 2096 | 2094 | -2 | 70 → 70 |
| 013 | 2263 | 2263 | +0 | 61 → 61 |
| 014 | 2011 | 2010 | -1 | 56 → 56 |
| 015 | 2294 | 2302 | +8 | 77 → 77 |
| 016 | 2177 | 2180 | +3 | 59 → 59 |
| 017 | 1941 | 1931 | -10 | 48 → 48 |
| 018 | 2157 | 2158 | +1 | 74 → 74 |
| 019 | 2200 | 2198 | -2 | 72 → 72 |
| 020 | 2352 | 2357 | +5 | 85 → 85 |
| **Tổng** | **43497** | **43486** | **-11** | |

## QA và continuity

- QA dự án trước/sau: PASS,20 chương chính thức,30 beat dàn ý,10 clue được theo dõi, `stage=chapter20_review`, không có chương ẩn vượt giới hạn.
- Bốn session `polish-prose --check`: PASS sau Literary Review độc lập gắn SHA từng nguồn/preview. Mỗi batch tối đa 5 chương. Không gọi apply.
- 108 tệp dự án có sẵn được so byte với baseline 239af1d: giữ nguyên toàn bộ. Bao gồm20 chương chính thức, approval, bible, outline, clue ledger, sealed solution và continuity. SHA 001 vẫn khớp `approved_sha256`; không cần giả lập hay làm mới phê duyệt.
- Reviewer đọc toàn bộ trước/sau và các chương giáp ranh; các lỗi nhỏ về so sánh chữ ký, thời điểm động tác, khả năng/thao tác hoàn tất, tư thế và chủ thể đã được sửa rồi review lại trước khi gắn SHA. Xem bốn `batchN-review.md`.
- Review toàn tuyến được ghi riêng ở `ARC_REVIEW.md`. Đây là đánh giá văn học/continuity của agent, không phải phê duyệt của độc giả hoặc blind-solver mới.

Các điểm kiểm soát xuyên tuyến:33 bậc/22 bậc thường chưa đồng nghĩa đã đo chắc chênh cao;T12 chưa được giải;042 không thêm nạn nhân;D1 không đổi thành T6;hai bản sao không thành hai nhân chứng;chu kỳ12 giờ còn là giả thuyết;chữ ký nhận bàn giao không thành tác quyền thiết kế hay bằng chứng có tội;N.V.Tín/17 hỗ trợ chứ chưa chốt danh tính;thương tích và nước ít là lời Linh;cuối 020 mới tới cửa kho, chưa lấy được hồ sơ.

Không dùng RAG/index nguồn trong lần này: không có Knowledge-RAG khả dụng; đọc trực tiếp tài liệu truyện đã xác định. Dự án dùng layout legacy phẳng, không có STORY_BRIEF.json hoặc state schema1; không tạo/migrate chúng.

## Vấn đề nội dung/tài liệu phát hiện — chưa sửa

1. `continuity/canon-log.md`, mục001, vẫn ghi chờ duyệt/chưa phải canon được phê chuẩn trong khi `approvals/approval.json` đã ghi duyệt 001 cùng SHA. Đây là mâu thuẫn tài liệu có trước baseline; giữ nguyên trong nhiệm vụ prose-only.
2. Outline dự kiến30 chương, bản hiện có20 chương. Dòng ghi trong canon log về các lần dừng 010 là lịch sử, không phải quyền viết tiếp. Arc chưa giải, chưa đóng; đây là trạng thái đang chờ đọc, không phải khoảng trống được phép tự bổ sung.
3. Chương 001 dùng “Hai mươi năm sử dụng”, trong khi bible/chronology.md đặt xây dựng 19 năm trước. Có thể là cách nói xấp xỉ; cần tác giả xác nhận, không đổi mốc trong preview.
4. Không phát hiện lỗi nội dung mới cần sửa qua các thay đổi preview. Những giới hạn chứng cứ đang mở là chủ ý cần bảo toàn, không bị “sửa cho rõ”. QA cơ học không chứng minh cốt truyện tuyệt đối đúng; kiểm định blind-solver thật vẫn là bước riêng theo dự án.

## Git và các commit batch

Branch riêng tạo từ 239af1d; không thay đổi main, không push/merge/force push. Không sửa skill toàn cục. Các commit dưới đây chỉ chứa preview, snapshot và hồ sơ review tương ứng.

- `cfecdf573ae9bf63dd2e1d1f9d910fa2f91359c9 — edit(arc1): preview prose polish for chapters 001–005`
- `41c69b78c7e5692b47856e3a3df1567490f721b3 — edit(arc1): preview prose polish for chapters 006–010`
- `e11c5978f641a72eb8cff2664b50e3f23a7533d8 — edit(arc1): preview prose polish for chapters 011–015`
- `88453833575ed15fd93201dc1991503ae156cd56 — edit(arc1): preview prose polish for chapters 016–020`

Style Guide, bản đọc ghép, full diff và báo cáo được commit riêng sau khi QA cuối hoàn tất; SHA commit hồ sơ được báo trong chat, tránh tự tham chiếu SHA trong chính commit đó.

## Cổng duyệt còn lại và bước apply

Quy tắc từ [ethan-novel-studio — PROSE_POLISH.md](/Users/ethannguyen/.codex/skills/ethan-novel-studio/references/PROSE_POLISH.md): **“Standalone preview: stop for user approval.”** Apply cần duyệt bản preview cụ thể; văn bản khóa cần quyền sửa rõ ràng. Vì vậy lần này dừng ở bộ20 preview đã review, không sửa metadata để mở khóa.

Bạn cần đọc rồi duyệt đúng 20 candidate cóSHA trong `word-counts.csv`, gắn với bốn session trên; đồng thời cho phép thay văn bản khóa, nhất là001. Ví dụ lời duyệt nếu chấp nhận: “Tôi duyệt20 preview001–020 của bốn session arc1-batch1 đến arc1-batch4 theo bảngSHA trong báo cáo, cho phép apply các bản này và sửa văn bản khóa kể cả chương 001; chỉ trên branch edit/bien-ban-sai-lech-prose-polish-arc1, không push hoặc merge.” Đây chỉ là mẫu, chưa phải lời duyệt đã nhận.

Sau lời duyệt thực tế, lượt apply phải kiểm lại nguồn, metadata, review và candidate SHA; nếu bạn yêu cầu sửa preview thì review SHA cũ hết hiệu lực.001 có nội dung mới sẽ cần cập nhật binding phê duyệt bằng quy trình được cho phép, lưu binding cũ và lời duyệt mới, không tự điền SHA để hợp thức hóa. Cổng `chapter20_review`, quyền viết 021, phê duyệt hoàn tất Arc 1 và quyền Arc 2 vẫn riêng biệt. Style Guide hiện là đề xuất; bạn có thể duyệt cùng bộ preview hoặc yêu cầu chỉnh giọng trước apply.
