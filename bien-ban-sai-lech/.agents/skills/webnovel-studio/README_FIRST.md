# BẮT ĐẦU Ở ĐÂY — Gói Webnovel Studio cho Codex

## Mục đích

Gói **tự chứa** một Codex skill, mã dựng dự án, dàn ý 30 chương, bí mật & manh mối arc đầu, chương 1 hoàn chỉnh và bộ kiểm tra. Không cần cài npm, pip, hay tải skill cộng đồng nào khác. Truyện mới **Biên Bản Sai Lệch** là tác phẩm nguyên bản, không dùng nhân vật/thiết lập/cốt truyện đặc trưng từ *Ngoạn Gia Hung Mãnh*.

## Cách A — để Codex tự làm toàn bộ (khuyến nghị)

1. Giải nén `skill.zip` ở một thư mục tùy ý; sau giải nén có thư mục `webnovel-studio/`.
2. Mở Codex Desktop với quyền truy cập thư mục vừa giải nén (hoặc dùng `codex` CLI ở đó).
3. Dán nguyên câu này:

   **"Đọc `webnovel-studio/README_FIRST.md` và `webnovel-studio/SKILL.md`. Tự chạy `webnovel-studio/scripts/bootstrap.sh` để tạo project riêng, cài skill ở project, init local git, commit, kiểm tra và biên tập chương 001. Xem `AGENTS.md`, kiểm thử logic và văn phong, cập nhật báo cáo rồi commit. DỪNG tại cổng duyệt chương 1, không viết chương 2. Báo đường dẫn project, commit hash và file chương để tôi đọc."**

4. Codex sẽ tạo thư mục `bien-ban-sai-lech` bên cạnh `webnovel-studio` theo mặc định. Trường hợp muốn dùng nơi khác, bảo Codex truyền đường dẫn mới vào script bootstrap.
5. Đọc `bien-ban-sai-lech/chapters/001.md`, trả lời yêu cầu sửa hoặc **"Tôi duyệt chương 1. Hãy viết tiếp toàn bộ arc 1 theo quy trình."**

## Cách B — dựng project thủ công (khi Codex không chạy được shell)

Mở terminal trong thư mục có `webnovel-studio/`:

```bash
bash webnovel-studio/scripts/bootstrap.sh
cd bien-ban-sai-lech
python3 .agents/skills/webnovel-studio/scripts/check_project.py .
```

Sau đó mở thư mục `bien-ban-sai-lech` bằng Codex và yêu cầu agent đọc `AGENTS.md`.

## Cổng duyệt bắt buộc

- Trạng thái ban đầu: `chapter1_review`, `approved=false`.
- Trước khi người dùng duyệt: được đánh giá/sửa chương 001, không được tạo `chapters/002.md` trở đi, kể cả draft ẩn.
- Chỉ sau lời duyệt **trực tiếp** từ người dùng, Codex mới được sửa `approvals/approval.json` với câu duyệt và đổi giai đoạn sang `arc1_writing`.
- Viết tiếp chương 2–30 theo lô 2–4 chương, kiểm tra và commit từng lô. Nếu không thể hoàn tất trong một phiên, báo tiến độ thực tế; không tự nhận làm nền hoặc hứa hoàn thành ở thời điểm khác.
- Sau arc 1: người dùng duyệt kết quả arc, Codex mới thiết kế và viết arc 2.

## Lưu ý Git và quyền truy cập

Script chỉ tạo thư mục **mới**, không đè thư mục có sẵn; commit là **local only**, không `push` và không sửa global Git config. Nếu máy chưa có Git identity, script đặt identity riêng ở repo mới là `Novel Studio Agent <novel-studio@localhost>` để commit chạy được. Bạn có thể đổi identity local sau.

## Cấu trúc đóng gói

`SKILL.md`: điều phối chung; `references/`: quy trình chuyên môn; `scripts/`: bootstrap + validator; `assets/project_template/`: project truyện đầy đủ (AGENTS, chapter 1, bible, outline, arc truth, memory, review, approvals).
