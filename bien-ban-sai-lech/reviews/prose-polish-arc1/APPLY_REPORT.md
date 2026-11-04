# Apply Prose Polish — chương 001–020

Ngày: 04/11/2026. Branch: `edit/bien-ban-sai-lech-prose-polish-arc1`. Baseline trước apply: `1451db2`.

## Phê duyệt thực tế

> Tôi duyệt bộ preview 001–020 vừa báo cáo. Apply cả 20 chương, cho phép sửa chương khóa 001 theo quy trình; giữ chapter20_review, chỉ trên branch riêng, không push hoặc merge.

Đã apply đúng 20 candidate có SHA trong [word-counts.csv](word-counts.csv), qua bốn session `arc1-batch1` đến `arc1-batch4`, dùng `--mode apply --allow-locked` và nguyên văn lời duyệt trên. Không biên tập thêm trong lượt apply. Style Guide tiếp tục là đề xuất riêng.

## Kiểm tra và kết quả

- Cả bốn session PASS kiểm nguồn, metadata, review gắn SHA và candidate trước mọi apply.
- 20/20 tệp chính thức sau apply khớp byte với preview đã duyệt và bảng SHA đã giao.
- Project QA PASS: 20 chương, chương 001 có 3069 đơn vị cách nhau bằng khoảng trắng, 30 beat outline, 10 clue, `stage=chapter20_review`, không có chương vượt giới hạn.
- Chỉ `chapter1.approved_sha256` thay đổi trong approval; toàn bộ trường khác giữ nguyên. Helper thực hiện cập nhật sau lời duyệt, không sửa thủ công để qua gate.
- SHA chương 001 cũ: `0600e9cb0fa75081896acf425f56fb87bf9b7aab74df013e24f14436caa90d7d`.
- SHA chương 001 mới: `4129f8118987cb087f138729607111571043f7e8d24399ca10c6198cd78037da`.
- Snapshot nguồn và metadata cũ vẫn nguyên SHA; manifest từng session lưu lời duyệt, thời điểm và lịch sử apply, `applied=true`.
- Apply các batch 006–020 trước, batch 001–005 sau cùng để cập nhật SHA001 chỉ khi các session khác đã kiểm xong metadata gốc; không sửa baseline hay review để bỏ qua kiểm tra.
- Bible, clue ledger, outline, sealed solution và toàn bộ continuity không thay đổi. Giữ writing cap20, Arc1 chưa hoàn tất, Arc2 chưa được duyệt; không viết021.
- [Mục lục bản chính thức](../../DOC_TRUYEN.md) đã cập nhật trạng thái. Các liên kết trỏ trực tiếp vào chương chính thức nên tự hiển thị đúng bản đã apply. [Bản ghép preview](PREVIEW_ALL.md) giữ nguyên để đối chiếu.

Hai điểm nội dung/tài liệu cũ đã báo vẫn chưa sửa: canon log001 ghi chờ duyệt; tuổi tòa nhà20năm so với chronology19năm. Chúng không được dùng để mở cổng hoặc sửa cốt truyện trong lần apply.

Chỉ commit cục bộ trên branch riêng; không push, merge hoặc đổi main. SHA commit apply được báo trong chat sau commit.
