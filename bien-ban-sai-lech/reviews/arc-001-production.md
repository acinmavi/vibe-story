# Nhật ký sản xuất arc 001 — tài liệu tác giả

## Phạm vi đã duyệt

Ngày 03/11/2026, người đọc duyệt chương 001 và yêu cầu viết hết arc 1, kiểm tra/commit từng lô, dừng sau arc. Theo kế hoạch có sẵn, đích là chương 030 (nằm trong khoảng 30–50 người đọc nêu). Chương 001 được khóa bằng SHA-256 trong approvals/approval.json. Không mở arc 002.

## Quy trình

Mỗi lô 2–4 chương: tác giả lập cảnh và giới hạn tri thức, viết tuần tự, sửa logic và văn; reviewer độc lập chỉ nhận chương đã viết và báo cáo blind trước đó, không nhận đáp án. Biên tập viên đối chiếu luật kín, sửa lỗi có chứng cứ, cập nhật continuity, chạy validator, kiểm tra độ dài/tên chương/hash chương001/diff rồi commit. Độ dài 1900–3000 đơn vị whitespace là mục tiêu mềm; mọi ngoại lệ phải có lý do cụ thể. Không dùng đếm chữ thay đánh giá văn học.

## Lô dự kiến

| Lô | Chương | Chặng | Trạng thái |
|---|---|---|---|
| 1 | 002–004 | Vòng an toàn; phiếu thiếu; bản ghi | hoàn tất, QA PASS |
| 2 | 005–007 | Hai sơ đồ; 00:12; người giữ chìa khóa | hoàn tất, QA PASS |
| 3 | 008–010 | Biển chỉ; áp lực tháo dỡ; vết vữa | hoàn tất; dừng chờ feedback |
| 4 | 011–013 | Thử sai; đầu dây; dự phòng hỏng | hoàn tất, QA PASS |
| 5 | 014–016 | Chữ ký; tên bị xóa; khe gió | hoàn tất, QA PASS |
| 6 | 017–020 | Sổ trực; lời khai; phản hồi; hai phương án | hoàn tất, QA PASS |
| 7 | 021–022 | Tiêu hủy; đối chiếu cao độ | chưa viết |
| 8 | 023–025 | T12; dữ liệu mất; cửa sổ 11 phút | chờ |
| 9 | 026–028 | Danh sách; tìm cửa; cứu người | chờ |
| 10 | 029–030 | Hậu quả; khép vụ án | chờ |

## Điểm kiểm soát

- Phân biệt tiếng gõ bất kỳ với bằng chứng chu kỳ; không nhận mọi tiếng gõ là tín hiệu sống.
- Giữ 33 bước, mốc đo phải so sánh độc lập; chì ngoài vùng còn thông tin.
- C01/C02 hiện diện từ001, C03 từ004; chưa giải cơ chế đầy đủ trước022–027.
- Linh/Thành phải có hành động tự cứu; Hạ Lam có quyền từ chối thử nguy hiểm.
- Tránh vô tình biến trì hoãn cứu hộ thành vô trách nhiệm; nêu lực lượng, nguồn lực, phương án đối chiếu và giới hạn tiếp cận.
- Thời gian từ đêm17 tới sáng20/10; ch00600:12 ngày18, kết nối đổi12giờ một lần, cao trào00:12 ngày20. Không cho người mắc kẹt tồn tại nhiều ngày thiếu nước mà bỏ qua hậu quả.
- Hồ sơ và công bố không là công tắc siêu nhiên; mở lối vật lý và phối hợp hai phía mới cứu được người.
- Mốc hoàn tất khác với người đọc duyệt arc. Giữ arc001_complete.approved=false và arc002.approved=false cho đến lời duyệt mới.

### Lô 1

Tác giả sửa hai lượt, blind review không blocker; góp ý vật liệu, lốiA và lịch đón sổ đã sửa. Cập nhật hỗ trợ cứu hộ chuyển vào005. Validator và kiểm hash/độ dài/diff chạy trước commit. Các chương002–004:1986/1900/1937 whitespace. Chương001 giữ nguyên.

## Thay đổi phạm vi theo người đọc

Người đọc yêu cầu “thôi tạm 10 chương rồi dừng ,tôi đọc sẽ cho feedback để tiêp sau”. Lượt này chốt chương010 và chờ feedback, không viết011. Đích toàn arc vẫn030 nhưng chưa hoàn thành. Dừng sớm hơn nếu quota còn15%; không dùng reset. Từ005 ba tác giả viết song song theo hợp đồng nối cảnh, root và blind reviewer kiểm chỗ nối trước commit lô.

### Lô 2

Ba tác giả viết theo handoff, root đọc cảba và blind review chỉ đọc prose. Sửa mốc07→06 trong005; bỏ cốc chưa có ở006; nối Thu bàn giao máy và kiểm tủ ngay đêm trong007, nêu giới hạn khảo sát tườngkín. Reviewer kiểm lại006–007 không blocker;005 sửa mốc sau lượt kiểm lại, root xác nhận thay đổi. Độ dài005/006/007:1958/2295/2331 whitespace. Validator/hash001/diff chạy trước commit.

### Lô 3 và bàn giao

Ba tác giả, hai lượt sửa mỗi chương; blind review không blocker. Root đọc cảba, sửa nguồn ảnh008 thành trí nhớ cógiới hạn, nối ghé6lấy túi, đổi010bắtđầu07:38 sau009rời sảnh07:30, bỏtừ gợi lịchsử chưa biết. Các sửa cuối do root kiểm, không nhận là người đọc thật đã duyệt. Chương008/009/010:2174/2168/2204 whitespace. Lối cứu hộ ngoàiB, liênlạc và đổi ca không dừng để chờsáng.

Đã có chương001–010;011–030 chưa viết. Người đọc muốn tạm10 để feedback, trạngthái chapter10_review, cap10. Không gọi arc đã hoàn tất hoặc tựmở arc002. Mục lục không tiết lộ đáp án: DOC_TRUYEN.md. Báo cáo, bí mật và kếhoạch vẫn trong thưmục tácgiả.

QA cuối: validator cấu trúc; kiểm đúng10chương liên tiếp; SHA256001 khớp bảnđã duyệt; count/heading mỗi chương mới; không011; các gate chưa duyệt vẫnfalse; diffcheck. Không suy QA máy thay đánhgiá văn học/độđộcđáo.

## Tiếp tục theo yêu cầu mới

Người đọc yêu cầu “viết tiếp 10 chương nữa đi , chưa hết quota”. Lượt mới viết011–020, vẫn dừng nếu quota còn15%. Không suy yêu cầu tiếp là lời phêchuẩn chi tiết toàn bộ002–010. Giữ001–010 nguyên vẹn, tiếp tục lô011–013,014–016,017–020; cập nhật mục lục khi xong.

### Lô011–013

Ba tácgiả, hai pass mỗi chương; blind khôngblocker. Root giới hạn rõ kếtluận camera, nối caThu. D1 riêngT6, chỉ phảnứng đôi chưa nhậndiện; backupngoài không đổi; hai đợt giờ mới là giảthuyết. Validator/hash001/diff/độdài kiểm trướccommit. Không sửa001–010.

### Lô014–016

Ba tácgiả/hai pass, blindkhôngblocker vịtrí/thờigian. Sửa014 mứcchắcchữký vs thựctếphátbản. C07seed, hồsơgiađìnhTín cónguồn, Lamchủđộngkhegió. Khôngsuyvuônggiólàcửahaynguyênnhân. Validator/hash001/diff/độdài trướccommit.

### Lô017–020 và bàn giao mới

Ba agent viết017–019,root020, hai pass và tíchhợp. Blind đọc prosekhôngsealed khôngblocker; agentkhácreviewlogic020 khôngblocker. Sửa ghế/chai/nguồn người đáp vàmứcchắc tên017→018. C08/C09seed, C10chưalệnhhủy. Kiểm20chương liên tiếp/heading/độdài/hash001/diff/001–010bấtbiến trướccommit. Dừng020đúngyêucầu,không021;quota cuối ghi theo côngcụ.
