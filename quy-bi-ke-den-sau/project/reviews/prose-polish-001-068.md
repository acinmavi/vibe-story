# Báo cáo hoàn tất biên tập văn phong — Arc 1 và Arc 2

Ngày 04/11/2026 · Nhánh `edit/prose-polish-arc1`.

Đã biên tập đủ 68 chương đã viết: Arc 1 (001–030), sau đó Arc 2 (031–068), theo phong cách chương 003 và STYLE_GUIDE được người dùng duyệt. Không viết thêm chương. Sau đối chiếu từng chương và review độc lập, không còn phát hiện thay đổi sự kiện, thứ tự, logic, timeline, nhân vật, manh mối hoặc giới hạn tri thức/năng lực do đợt sửa này gây ra.

- [Đọc liền Arc 1](../ARC_001.md) · [Đọc liền Arc 2](../ARC_002.md) · [Mục lục từng chương](../DOC_TRUYEN.md).
- [Đối chiếu từng chương Arc 1](arc-001-prose-polish.md) · [Đối chiếu từng chương Arc 2](arc-002-prose-polish.md).
- [STYLE_GUIDE](../STYLE_GUIDE.md) · [QA và SHA trước/sau từng chương](prose-polish-qa.json).

## Những thay đổi văn phong

Nối những câu ngắn cùng mô tả một động tác hoặc lượt quan sát; đưa phản ứng và cảm giác đã có vào cạnh việc đang diễn ra. Rà lại đại từ, chủ thể, câu lược và cách kết hợp từ để tiếng Việt rõ hơn. Tách lại khi câu ghép dài hoặc chứa nhiều người thực hiện. Không thêm bối cảnh, suy nghĩ, lời thoại hay giải thích lore để làm đầy chương.

Mức sửa không chia đều theo số lượng câu. Những đoạn đối thoại, phát hiện, đe dọa, do dự và quyết định vốn có nhịp tốt được giữ. Chương 037 và 067 chỉ sửa vài đoạn; các chuỗi thao tác giấy ở đầu Arc 1 được can thiệp nhiều hơn. Không tìm cách làm tất cả các câu dài hơn.

Các nhịp ngắn giữ lại gồm “Rất gần.” ở 001, “Anh tháo dây.” ở 003, “Quá sớm.” ở 010, hai đoạn Nell ghi rồi giữ bút ở 040 và những nhịp đếm trong cao trào 063. Lời thoại không thay chữ. Bí ẩn vẫn nằm trong chi tiết quan sát và những điều nhân vật chưa thể biết.

## Thống kê

“Từ” được đếm bằng khoảng trắng (`split()`), gồm tiêu đề chương; không phải số từ vựng tiếng Việt. Cùng cách đếm cho trước/sau.

| Phạm vi | Trước | Sau | Chênh lệch |
|---|---:|---:|---:|
| Arc 1 | 64,256 | 64,374 | +118 (+0.184%) |
| Arc 2 | 70,926 | 71,016 | +90 (+0.127%) |
| Tổng68 chương | 135,182 | 135,390 | +208 (+0.154%) |

Bảng từng arc ghi số đoạn trước/sau. Phần lớn ranh đoạn giữ nguyên; 031 nối hai khối kể cùng một nhịp. Độ dài toàn bộ chỉ tăng khoảng 0,15%, không kéo dài để đạt chỉ tiêu. Từng chương vẫn trong khoảng 1.800–3.000 đơn vị theo cách đếm trên.

## Mười ví dụ trước/sau

Các đoạn dưới lấy từ commit nguồn và bản cuối, không phải đề xuất chưa áp dụng.

### Chương 001 — Nối ý muốn nói với sự ngập ngừng.

**Trước:**

> Trần Duy muốn hỏi đây là đâu. Lời nói đã đến môi thì dừng lại.

**Sau:**

> Trần Duy muốn hỏi đây là đâu, nhưng lời đã đến môi lại dừng.

### Chương 003 — Gom các kết quả cùng loại, giữ nhịp dừng ở dấu đỏ.

**Trước:**

> Mã kiện đúng. Số hòm đúng. Chữ chỉ loại hàng giống nhau. Có một chữ viết tắt anh không hiểu, nhưng nó xuất hiện ở cùng vị trí trên cả hai bản. Anh ghi nó vào mảnh báo lỗi để hỏi sau, không tự đổi thành từ khác.

**Sau:**

> Mã kiện và số hòm đều khớp, chữ chỉ loại hàng cũng giống nhau. Chỉ có một chữ viết tắt anh chưa hiểu, xuất hiện ở cùng vị trí trên cả hai bản; anh ghi vào mảnh báo lỗi để hỏi sau, chứ không tự đổi thành từ khác.

### Chương 011 — Nối động tác lấy thiếp với chi tiết trên vật.

**Trước:**

> Ông ra quầy, trở lại với tấm thiếp màu kem. Chữ Iona Vale in nhỏ, bên dưới là nghề giám định sách và chứng từ. Có địa chỉ, giờ tiếp khách theo hẹn, không có hình vẽ trang trí.

**Sau:**

> Ông ra quầy rồi trở lại với tấm thiếp màu kem, trên đó tên Iona Vale được in nhỏ, bên dưới ghi nghề giám định sách và chứng từ. Thiếp có địa chỉ, giờ tiếp khách theo hẹn, không có hình vẽ trang trí.

### Chương 019 — Giữ giới hạn của việc nhìn trong cùng câu.

**Trước:**

> Một lúc sau, anh thử mở mắt nhìn mép chăn. Không tìm ý nghĩa trong các sợi vải. Khi những đường nhỏ bắt đầu sắc lên quá mức, anh quay mắt về phần tường tối, rồi nhắm lại.

**Sau:**

> Một lúc sau, anh thử mở mắt nhìn mép chăn mà không tìm ý nghĩa trong các sợi vải. Đến khi những đường nhỏ bắt đầu sắc lên quá mức, anh quay mắt về phần tường tối rồi nhắm lại.

### Chương 025 — Liên kết điều không thấy với điều nghe được.

**Trước:**

> Evan không thấy hắn đi lúc nào. Anh nghe tiếng người bán bảo tránh khỏi cửa, rồi một cỗ xe lăn đi. Chiếc chuông trên đầu anh đã ngừng rung mà âm thanh vẫn mắc trong tai.

**Sau:**

> Evan không thấy hắn đi lúc nào, chỉ nghe người bán bảo tránh khỏi cửa rồi tiếng một cỗ xe lăn đi. Chiếc chuông trên đầu đã ngừng rung mà âm thanh vẫn mắc trong tai anh.

### Chương 031 — Nối nhận ra và phản ứng, giữ riêng hành động mỗi người.

**Trước:**

> Evan gật. Anh xin một cốc nước, được bà đẩy chiếc cốc sứ sứt quai qua. Lúc uống, anh nhận ra mình đang nhìn những mẩu vụn trên bàn. Anh quay mặt đi hơi muộn.

**Sau:**

> Evan gật rồi xin một cốc nước. Bà đẩy chiếc cốc sứ sứt quai qua; lúc uống, anh nhận ra mình đang nhìn những mẩu vụn trên bàn và quay mặt đi hơi muộn.

### Chương 042 — Nối thao tác ghi nhưng giữ giới hạn khái quát.

**Trước:**

> Rowe ghi hai lần vật qua. Ông ghi thêm lần của mình trước đó, không viết rằng đã biết mọi người sẽ gặp cùng một chuyện. Marsh hỏi ông có chóng mặt hoặc đau đâu không. Ông nói chưa, để bà nhìn mắt và kiểm bàn tay ngay ngoài lối.

**Sau:**

> Rowe ghi hai lần vật qua rồi ghi thêm lần của mình trước đó, không viết rằng đã biết mọi người sẽ gặp cùng một chuyện. Marsh hỏi ông có chóng mặt hoặc đau đâu không; ông nói chưa, để bà nhìn mắt và kiểm bàn tay ngay ngoài lối.

### Chương 054 — Nối phản ứng, quan sát và ký ức đã có.

**Trước:**

> Câu trả lời làm Evan ngẩng đầu khỏi trang. Anh nhìn cửa thấp đang mở, nhớ những lần đứng ngoài gọi mà không ai đáp.

**Sau:**

> Câu trả lời làm Evan ngẩng đầu khỏi trang, nhìn cửa thấp đang mở và nhớ những lần đứng ngoài gọi mà không ai đáp.

### Chương 055 — Giữ thứ tự ngồi, lấy vải, lau và chạm dụng cụ.

**Trước:**

> Nell ngồi xuống cạnh hộp. Cô lấy mảnh vải sạch lau bàn tay trước khi chạm phần dụng cụ đã đo.

**Sau:**

> Ngồi xuống cạnh hộp, Nell lấy mảnh vải sạch lau bàn tay trước khi chạm phần dụng cụ đã đo.

### Chương 066 — Sửa kết hợp từ, giữ nguyên giới hạn chấn thương.

**Trước:**

> Anh nằm thêm một lúc, thử thả vai mà không xoay cổ tay phải.

**Sau:**

> Anh nằm thêm một lúc, thử thả lỏng vai mà không xoay cổ tay phải.

## Rủi ro đổi nội dung đã kiểm và xử lý

| Nguy cơ | Cách giữ nghĩa trong bản cuối |
|---|---|
| Câu phụ đổi người thực hiện | 003 giữ **hai người cùng đặt bó bìa**, không thành động tác riêng Mara. 036 không tự gán Nell đặt hộp từ câu bị động. |
| Nối bối cảnh thành vị trí chưa nêu | 003 bỏ vị trí Gideon “bên bàn” xuất hiện trong bản thử; ông ở trong kho và đồ trên bàn vẫn là hai thông tin riêng. |
| Hành động hoàn tất bị đổi thành mục đích | 033 giữ bà Finch **đã chép** địa chỉ. 038 giữ Agnes **đã so bảng/thùng và chuyển phương án**. 039 giữ Evan **đã nhắc, đối vạch, viết**. 041 giữ Agnes **đã ghi** thời gian. Những chữ “để” làm mất xác nhận hoàn tất đã được bỏ/hoàn nguyên. |
| Tự chốt một đại từ | 058 không thêm “nhìn nó” để xác định đối tượng nhìn là thước. 062 giữ “nó” trong câu đặt xuống, không tự chọn giấy thay vì tay trái. |
| Quan sát bị nâng thành nhân quả | Giữ khối nặng hạ/dây căng034 là quan sát; không biến mảnh vữa rơi047 thành khẳng định vừa để lộ đầu neo. |
| Động tác, số lượng, trạng thái bị thay | Không đổi “nhận” thành “lấy” ở 057; không thêm nhiều người/đèn053 hoặc nhóm người trở lại sân057. 028 giữ thói quen kéo ghế, không thành ghế dành riêng. |
| Mức chắc chắn hoặc nguồn bị lệch | Giữ cầm phiếu/ký nhận, kho xe/kho sau,317/371, nhớ từ sách/đã kiểm, chưa rõ/đã xác nhận. 029 không chuyển “tìm” thành “tìm thấy”. Lời nhân chứng còn đủ giới hạn. |
| Manh mối bị giải thích thêm | Rãnh ép vẫn là nét rời, không thành tên/câu trọn; 030 không quy nét thiếu thành lỗi Evan vẽ. |
| Tiền, ngày, quyền hạn | Giữ khoản tiền/hạn nợ, ngày thư viết/gửi/nhận, quyền giữ gốc/sao, tiền trả kỳ31/8 và kỳ tháng9 chưa chốt. 068 giữ vị trí từ “trước” trong thủ tục nhận tiền. |
| Cơ cấu, năng lực, cao trào | Giữ A/B, D1/D2, lối ngoài/lối riêng,22/25/40 giây và phép thử 5 giây khác nhau; không đổi thử vật thành thử người, không cấp kỹ năng/tri thức hoặc làm chấn thương tự hết. |

Các điểm trên được xử lý bằng sửa hẹp hoặc giữ câu gốc. Những chỗ mơ hồ có sẵn không được tự “giải đáp” trong đợt biên tập văn phong. Không sửa sự kiện nền để câu dễ nối hơn.

003.polished.md vẫn là mốc thử phong cách đã duyệt. Chương 003 giữ phong cách ấy, có hai hiệu chỉnh bảo toàn nội dung sau review: trả lại chủ thể hai người đặt bìa và bỏ vị trí đứng bên bàn chưa được bản gốc xác nhận. Bản thử không được ghép thêm vào truyện chính.

## QA và review cuối

Đã đọc từng chương và phần nối, so phần thay đổi với nguyên bản/continuity. Review độc lập bao phủ001–030,031–050,051–068. Các findings về chủ thể, hành động hoàn tất, đại từ và cách kết hợp từ đã được xử lý. Câu060 “đủ cách xa nhau” đã sửa thành “cách nhau đủ xa”. Không còn finding chưa xử lý trong phạm vi sửa.

Kiểm máy đủ 68 chương: giữ tiêu đề; nguyên chuỗi chữ số, mọi đoạn trong ngoặc kép cong và ngoặc đơn cong theo thứ tự; số từ/đoạn và SHA trước/sau được ghi trong JSON QA. Những phép kiểm này không tự chứng minh tương đương toàn bộ ngữ nghĩa; phần nghĩa được đối chiếu bằng đọc soát.

`python3 .agents/skills/quy-bi-ke-den-sau/scripts/check_project.py .`: PASS,68 chương chính thức, stage `arc2_complete`, cap 68 giữ nguyên. `git diff --check`: PASS. Hai bản đọc liền đã so đủ 68 phần với từng tệp nguồn; số từ trong mục lục/README đồng bộ.

Bible, continuity, kế hoạch, Arc 3 và script QA không bị sửa. Không có069, cảnh mẫu hoặc quyền viết mới.

## Git và hồ sơ duyệt

Nguồn trước sửa: `8e838312e8c5560d00e637a4feaf08613f67989c`. Bản cũ còn đầy đủ trong Git. Các nhóm commit biên tập không quá5 chương; commit sửa sau review cũng chỉ1–4 chương. Không push hoặc merge.

Khóa SHA001 được cập nhật theo yêu cầu cho sửa toàn Arc 1. SHA duyệt gốc, nguyên văn và thời điểm duyệt ban đầu được giữ; bổ sung căn cứ cho phép biên tập và SHA mới. Các cờ `approved`, trạng thái hoàn tất arc, quyền chuẩn bị Arc 3 và khóa 069 không thay đổi.

Thông báo hoàn tất dùng skill ethan-completion-notifier do người dùng trực tiếp yêu cầu, sau khi kiểm và commit xong.
