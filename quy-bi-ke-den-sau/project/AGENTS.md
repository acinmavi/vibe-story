# BẮT BUỘC: lệnh dành cho Codex trong project này

Đọc `README.md`, `bible/canon-anchors.md`, `bible/world.md`, `bible/characters.md`, `bible/power.md`, `bible/tarot-and-world.md`, `arcs/arc-001/arc-spec.md`, `arcs/arc-001/solution-sealed.md` (writer/designer only), `arcs/arc-001/outline.md`, và `continuity/` trước mọi hành động sáng tác.

- Phục vụ yêu cầu viết đồng nhân *Quỷ Bí Chi Chủ* theo canon phần 1, không dùng mặc định thông tin phần 2 vào năm 1349.
- Thời điểm mở đầu 28/6/1349, cùng ngày Klein tỉnh; MC không nhận ra ngay truyện, phải tự sống và xác minh thế giới.
- Hội Tarot đã thành lập trong ngày 28/6/1349, nhưng MC không tham gia ở Tingen. Đến giai đoạn Cattleya vốn gia nhập, MC có thể thay cô nhận lá Ẩn Giả với nguyên nhân AU thuyết phục. Cattleya vẫn tồn tại, hữu dụng và độc lập.
- Sau khi vào Tarot, nhân vật có cơ hội đổi tri thức lấy nguồn lực nhưng có cái giá và rủi ro; tăng dần những cuộc hợp tác với Thế Giới thành tình bạn. Klein tự điều tra nguồn gốc chung qua mạng lưới của anh và Nguyên Bảo; MC không trực tiếp giúp cuộc điều tra đó. Theo dõi ba sổ continuity mới.
- BẮT BUỘC: **Hội Tarot không phải diễn đàn để MC thể hiện biết tuốt.** MC bảo vệ danh tính Klein/Thế Giới/Ngu Giả, tôn trọng Ngu Giả, không sửa hoặc giải thích hộ ông; mọi buổi họp giữ quyền chủ động và uy nghiêm Ngu Giả, cho các thành viên khác góp ý. Đọc `bible/tarot-etiquette.md` và `references/tarot-etiquette.md`, cập nhật `continuity/tarot-meeting-ledger.json`.
- Mọi cảnh chiến đấu với The World: điền cấp danh sách, kỹ năng đã đạt, vật phẩm, giới hạn và cái giá theo `bible/combat-duos.md`. Các giao điểm Cattleya → Bernadette → Klein phải theo `bible/cattleya-bernadette.md`; không biến họ thành NPC cho MC thăng cấp.
- MC theo con đường Ẩn Giả: có kiến thức *đọc truyện* về phương pháp nhập vai nhưng không có công thức, nguyên liệu, tín nhiệm, tiền bạc. Không ai tự đưa potion cho miễn phí.
- Dấu ấn sương mù xám là AU, chỉ giảm một số rủi ro kiến thức; không phải Sefirah Castle duplicate, không cho dịch chuyển, miễn dịch, resurrection.
- Vụ cuốn sổ Antigonus của Welch/Klein là canon. Vụ xưởng in mục lục trong ARC 1 hoàn toàn original AU, không đánh đồng hoặc bóc mật mã của canon.
- Thông tin bài báo Welch/Naya là AU; báo không in chi tiết cuốn sổ. Nếu có mốc ngày còn chưa chắc, ghi mốc tương đối và nguồn.
- KHÓA DUYỆT: `approvals/approval.json` mặc định `chapter1_review`. Nếu chưa có lời duyệt người dùng cho chương 001, chỉ review/chỉnh chương 001 rồi QA/commit; **không** viết hoặc giấu chương 002. Không nhận suy đoán làm phê duyệt.
- Nếu được duyệt, cập nhật `approval.json` với văn bản duyệt nguyên ý, thời điểm UTC và SHA256 chương 001; giữ nguyên chương 001 đã duyệt cho đến khi người dùng yêu cầu sửa.
- Viết chương 2–30 theo các lô 2–4; mỗi lô cập nhật continuity, kiểm tra rồi commit local. Không remote, không push, không thay repo khác, không chạy ở nền.
- QA: `python3 .agents/skills/quy-bi-ke-den-sau/scripts/check_project.py .`.
- Trong các cảnh dùng lore, ưu tiên câu chuyện hơn trình bày từ điển. Không sao chép diễn biến hay đoạn hội thoại nguyên tác.
- BẮT BUỘC đọc `bible/narrative-contract.md` trước thiết kế hoặc viết tiếp: cuối arc tăng tốc bằng các tuyến đã gieo hội tụ và hệ quả nối nhau, không phá mạch chung; trả các chi tiết đã hứa với độc giả; ngày tháng, năng lực, tri thức và phong cách nhân vật phải nhất quán. Thay đổi cần nguyên nhân và quá trình; lệch bất thường phải được nhận thấy, gieo dấu và giải thích có nhân quả.
- Theo dõi `continuity/setup-payoff-ledger.md` cùng `continuity/open-loops.json`. Không đánh dấu đã trả chỉ vì tác giả có ý định dùng sau. Trước Arc2 phải bổ sung kiểm kê chi tiết còn thiếu và chốt mốc tái xuất/trả cho các tuyến mở; cổng duyệt Arc2 giữ nguyên.

## Chỉ thị người dùng04/11/2026 — hiệu lực cho phần tiếp theo

Arc3chọnA“Giá của một cái tên”:chỉchuẩnbị,chưaduyệtdànýhoặcviết069. Sau khi được phép viết, **mỗi chương hoàn tất phải review/QA/cập nhật continuity và COMMIT RIÊNG trước khi viết chương kế tiếp**. Không gộp nhiều chương một commit; quy tắc này thay lịch commit theo lô cũ. Push chỉ theo yêu cầu, không force-push.
