# Tiến độ dịch — Quỷ Bí: Từ Đọc Giả Bắt Đầu

Cập nhật: 2026-11-06 — sau lượt dịch chương 11–16

- Trạng thái: **Đang thực hiện; chưa hoàn thành; chưa có EPUB cuối cùng**.
- Đã dịch và biên tập, có file kiểm tra được: **16 chương**, `chapters/0001.md` đến `chapters/0016.md`.
- Chương cần làm tiếp: **0017**.
- Nguồn ZIP/HTML do người dùng gửi trong ChatGPT; chưa commit nguồn tiếng Trung lên GitHub.
- Bộ dữ liệu đã xử lý ở phiên trước: **1.578 mục**, trong đó **2 mục còn thiếu**; **không được xem 1.578 là số chương đầy đủ đã kiểm chứng với bản gốc**.
- Mục tiêu cuối cùng: **một EPUB tiếng Việt có đầy đủ chương nguồn hợp lệ, không thay thế các chương chưa dịch bằng bản gốc tiếng Trung**.

## Checklist mỗi đợt

- [x] Tạo nhánh làm việc riêng và folder dự án
- [x] Lưu bản dịch biên tập chương 0001
- [x] Lưu bản dịch biên tập chương 0002
- [x] Dịch và commit chương 0003–0006
- [x] Dịch và commit chương 0007–0010, đối chiếu điểm đầu/cuối và các tình tiết chính với nguồn trong `chapters.jsonl`
- [x] Tạo lịch tự động dịch tiếp mỗi giờ (khả năng truy cập nguồn trong phiên tự động cần kiểm chứng)
- [ ] Bổ sung nội dung nguồn bị thiếu/nhầm ở các ngoại truyện
- [x] Dịch và commit chương 0011–0016 (đối chiếu theo từng đoạn nguồn)
- [ ] Dịch từ chương 0017 trở đi, tuần tự, có đối chiếu nguồn
- [ ] QA tổng thể: đúng số chương, thứ tự, tên, thuật ngữ, không thiếu đoạn
- [ ] Đóng gói **duy nhất một EPUB hoàn chỉnh** và kiểm tra bằng EPUBCheck

## Quy tắc trạng thái

Mỗi lần dịch xong một chương, commit bản `chapters/NNNN.md` và cập nhật dòng **Chương cần làm tiếp**. Không đánh dấu hoàn thành nếu chương mới chỉ dịch nháp hoặc chưa đối chiếu. Từng chương được commit tuần tự. Lịch tự động tiếp tục vào các lượt sau nếu có thể truy cập đúng file nguồn; nếu không, phải ghi blocker, không tự bịa.

## Cách yêu cầu tiếp tục

> Tiếp tục dịch Quỷ Bí: Từ Đọc Giả Bắt Đầu trong acinmavi/vibe-story, nhánh translation/quy-bi-doc-gia-20261106. Đọc PROGRESS.md, dịch các chương kế tiếp từ bản nguồn tôi đã cung cấp, commit từng chương và cập nhật tiến độ. Chỉ xuất EPUB khi hoàn thành toàn bộ.


## Cập nhật chương 3–6

- 0003 — Những điểm đáng ngờ — commit `fb539505`.
- 0004 — Làm quen — commit `2cc035b2`.
- 0005 — Xio và Jane — commit `af32f588`.
- 0006 — Cuộc tụ họp Phi Phàm — commit `624de8c9`.
- Lượt chạy theo lịch đầu tiên truy cập thành công hai file ZIP nguồn do người dùng cung cấp và commit chương 0007–0010. Vẫn phải kiểm tra quyền truy cập nguồn trong từng lượt kế tiếp.
- Repo công khai: cần xác minh quyền phân phối bản dịch trước khi công bố rộng rãi.

## Lượt dịch tiếp theo — 2026-11-06

Đã xác minh sự hiện diện trên nhánh của các bản dịch đầy đủ sau:

| Chương | Tiêu đề tiếng Việt | Commit |
|---|---|---|
| 0007 | Thử thách của Mắt Trí Tuệ | `8e605dc3` |
| 0008 | Người Đọc Danh Sách 9 | `4d90af7c` |
| 0009 | Lời nguyền | `6cf60311` |
| 0010 | Cầu viện | `a3909098` |

**Chương tiếp theo trong lượt trước:** `0011`. Nguồn khôi phục thành công từ ZIP người dùng: `341776.zip` và `quy_bi_doc_gia_du_an_dich_epub.zip` (bên trong có `qb_dich/chapters.jsonl`). Mỗi bản dịch trên được đối chiếu theo nội dung chương tương ứng, chưa phải kiểm định toàn bộ sách. Không đưa các ZIP nguồn lên repository công khai.

## Lượt dịch tiếp theo — 2026-11-06 (chương 11–16)

Đã đọc ba file hướng dẫn, đối chiếu danh sách chương trên GitHub và dữ liệu gốc từ `qb_dich/chapters.jsonl` bên trong ZIP do người dùng cung cấp. Xác nhận 16/16 file chương từ 0001 đến 0016 đều tồn tại trên nhánh, không có lỗ hổng số thứ tự.

| Chương | Tiêu đề tiếng Việt | Commit tạo file |
|---|---|---|
| 0011 | Trừ tà | `2802da97` |
| 0012 | Truy tìm | `18f86ae2` |
| 0013 | Thẩm vấn | `37370bbd` |
| 0014 | Trang viên bỏ hoang | `ce4e4397` |
| 0015 | Huấn luyện | `ef3ba4a4` |
| 0016 | Ma pháp nghi thức | `db98360d` |

**Chương cần dịch tiếp:** `0017` (`第17章…`, tên chương cần đọc trực tiếp từ nguồn ở lượt sau). Đã đối chiếu diễn biến và điểm kết thúc của từng chương với bản gốc; chưa thực hiện một lượt kiểm định độc lập toàn bộ nội dung, vì vậy chưa đánh dấu QA tổng thể.

**Nguồn bị thiếu ở phần ngoại truyện** vẫn giữ nguyên tình trạng ghi trong `SOURCE_GAPS.md`.
