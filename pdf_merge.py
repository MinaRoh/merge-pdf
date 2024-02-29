import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_current_directory(output_filename="merged.pdf"):
    # 현재 디렉토리에서 PDF 파일 목록 가져오기
    pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]

    # PDF 파일이 없으면 메시지 출력 후 종료
    if not pdf_files:
        print("현재 디렉토리에 PDF 파일이 없습니다.")
        return

    # 파일 이름을 기준으로 정렬
    pdf_files.sort()
    
    # PdfMerger 인스턴스 생성
    merger = PdfMerger()

    # 모든 PDF 파일을 병합
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    # 결과물 파일 저장
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)

    print(f"PDF 파일이 성공적으로 병합되어 '{output_filename}'로 저장되었습니다.")

if __name__ == "__main__":
    merge_pdfs_in_current_directory()
