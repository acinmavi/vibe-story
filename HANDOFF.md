# Handoff — Quỷ Bí Chi Chủ: Kẻ Đến Sau

Ngày04/11/2026. Chỉ làm trong repository hiện tại: `/Users/ethannguyen/Documents/20261103/vibe-story/quy-bi-ke-den-sau/project`.

## Yêu cầu và cổng hiện tại

Arc1 và Arc2 đã hoàn tất. Người dùng vừa yêu cầu ghi handoff **vào repo** rồi push; vị trí này ưu tiên hơn thư mục Temp mặc định của skill. Yêu cầu push không mở quyền viết truyện mới. **Dừng sau068, không069/Arc3 nếu chưa có phê duyệt mới.** Không tạo repository mới, không cài lại skill; giữ thay đổi chưa commit của người dùng.

Nguồn trạng thái chuẩn:

- [README](README.md), [checkpoint](SESSION_STATE.md), [approval](approvals/approval.json).
- [Memory hiện tại](continuity/CURRENT_STATE.md), [bốn tầng tri thức](continuity/KNOWLEDGE_LEDGER.md), [năng lực/đồ/tiền](continuity/POWER_AND_ITEMS.md).
- [Bàn giao Arc1](arcs/arc-001/FINAL_RECAP.md), [bàn giao Arc2](arcs/arc-002/FINAL_RECAP.md), [QA kếtArc2](reviews/arc-002-completion.md).
- [Đọc truyện](DOC_TRUYEN.md), [Arc1](ARC_001.md), [Arc2](ARC_002.md).

Không chép lại nội dung các hồ sơ này vào kế hoạch mới. Khi có mâu thuẫn, đối chương đã viết và ngày nguồn; kế hoạch lịch sử không tự thành sự kiện.

## Điều phiên sau phải giữ

Commit hoàn tấtArc2: `45e455beb86b86de860068912cd0987095f9f62a`. Review độc lập đủ031–068 và review tích hợp đã PASS; chi tiết kiểm, số chương/từ và giới hạn lore nằm trong báo cáo QA. Chương001 được duyệt và đóng băng; lần hoàn tấtArc2 giữ nguyên001–040. Không sửa chương cũ chỉ để hợp ý tưởng mới.

Câu hỏi gần nhất của người dùng là progress sau hai arc; đã giải thích MC ở Tingen/Seq9 cuốiArc1, Backlund/vẫnSeq9 cuốiArc2. Chưa có yêu cầu tăng bậc hoặc phê duyệtArc3 từ câu hỏi ấy. Dùng memory cho ngày, mức tiêu hóa, tiền, nghĩa vụ và quyền tra nguồn thật; không tự cấp công thứcSeq8.

[Ba hướngArc3](arcs/arc-003/OPTIONS.md) là đề xuất, A được khuyến nghị nhưng **chưa duyệt**. [Đánh giá đường dài](long-game/POST_ARC_002_ASSESSMENT.md) và [sổ lời hứa](continuity/setup-payoff-ledger.md) ghi các quyết định/mốc phải xử lý: chính sáchNeil, nguồn tin nhắn/giọng mình ở cấp tác giả, hậu quảTingen và đờiEvan. Cần chốt các cổng này trước bản thảo; không bỏ qua do tiến độ chương.

## Cách tiếp tục

ĐọcAGENTS.md và skill local `.agents/skills/quy-bi-ke-den-sau/SKILL.md`, sau đó các hồ sơ trên theo nhiệm vụ thực tế. Gợi ý skill: `caveman` cho trao đổi ngắn; `using-superpowers` cho công việc nhiều bước; skill novel cho thiết kế/viết/review; `handoff` khi chuyển phiên. Văn chương vẫn là tiếng Việt tự nhiên, không viết kiểu nén chat.

Mọi lệnh shell bắt đầu bằng `rtk`. Theo dõi việc nhiều bước bằng `work_state_read(includeClosed=true)`/`work_state_write`; không đóng các list của truyện khác. KiểmGitstatus/remotes/branch trước thao tác; chỉ stage tệp thuộc việc mình. Push đã được người dùng yêu cầu, nhưng phải xác định repo/branch đích và kiểm kết quả remote; không suy URL từ một dự án khác. Không force-push hoặc ghi đè lịch sử remote để giải quyết xung đột.

Nếu được duyệt viết tiếp: cập nhật approval có chứng cứ, đối nguồn canon/tri thức/năng lực, viết theo lô2–4, review độc lập và QA trước commit. Các lệnh QA đã có trong báo cáo; không cài framework mới. Không coi script PASS là chứng minh truyện không có hố.
