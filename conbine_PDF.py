import os
from pypdf import PdfReader, PdfWriter

def interleave_pdfs(path1, path2, output_path):
    # 检查文件是否存在
    if not os.path.exists(path1) or not os.path.exists(path2):
        print("错误：找不到输入的 PDF 文件，请检查路径是否正确。")
        return

    try:
        # 读取两个 PDF 文件
        reader1 = PdfReader(path1)
        reader2 = PdfReader(path2)
        writer = PdfWriter()

        # 获取页数
        len1 = len(reader1.pages)
        len2 = len(reader2.pages)
        
        # 取最大页数作为循环依据
        max_pages = max(len1, len2)

        print(f"正在合并...\nPDF1 共 {len1} 页\nPDF2 共 {len2} 页")

        # 循环合并
        for i in range(max_pages):
            # 如果 PDF1 还有页码，添加 PDF1 的第 i 页
            if i < len1:
                writer.add_page(reader1.pages[i])
            
            # 如果 PDF2 还有页码，添加 PDF2 的第 i 页
            if i < len2:
                writer.add_page(reader2.pages[i])

        # 保存结果
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        
        print(f"成功！合并后的文件已保存为: {output_path}")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    print("--- PDF 交叉合并工具 ---")
    
    # 获取用户输入
    # pdf1_path = input("请输入第一个PDF文件的路径 (例如 a.pdf): ").strip(' "\'')
    # pdf2_path = input("请输入第二个PDF文件的路径 (例如 b.pdf): ").strip(' "\'')
    # output_filename = input("请输入输出文件名 (默认 merged.pdf): ").strip(' "\'')
    pdf1_path = "pdf_path"
    pdf2_path = "pdf_path"
    output_filename = "pad_path/pdf_name"

    # 设置默认输出文件名
    if not output_filename:
        output_filename = "merged.pdf"
    
    # 确保输出文件名以 .pdf 结尾
    if not output_filename.lower().endswith(".pdf"):
        output_filename += ".pdf"

    # 执行合并
    interleave_pdfs(pdf1_path, pdf2_path, output_filename)