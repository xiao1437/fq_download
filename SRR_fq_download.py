import os
import argparse
parser = argparse.ArgumentParser(description="使用ascp批量下载fq文件")
parser.add_argument("-k", "--key", type=str, default="0", help="输入ascp密匙文件路径")
parser.add_argument("-t", "--type", type=str, default="0", help="输入1为单端数据，2为双端数据")
parser.add_argument("-i", "--input", type=str, default="0", help="输入批量下载数据汇总文件路径，文件输入内容需为  SRR号/存放对应fq文件的目录")
args = parser.parse_args()
def single_seq():
    with open(args.input, "r", encoding="UTF-8") as f:
        for x in f:
            list1 = x.strip().split("/")
            if list1[1]:
                os.system(f"mkdir {list1[1].strip()}")
                srr_num = list1[0].upper().strip("SRR").strip()
                if len(srr_num) == 6:
                    os.system(f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/SRR{srr_num}/SRR{srr_num}.fastq.gz {list1[1].strip()}")
                elif len(srr_num) == 7:
                    os.system(f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/00{srr_num[-1]}/SRR{srr_num}/SRR{srr_num}.fastq.gz {list1[1].strip()}")
                elif len(srr_num) == 8:
                    os.system(f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/0{srr_num[-2:]}/SRR{srr_num}/SRR{srr_num}.fastq.gz {list1[1].strip()}")
                else:
                    print(f"{srr_num}填写错误")
                    continue
            else:
                srr_num = list1[0].upper().strip("SRR").strip()
                if len(srr_num) == 6:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/SRR{srr_num}/SRR{srr_num}.fastq.gz ./")
                elif len(srr_num) == 7:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/00{srr_num[-1]}/SRR{srr_num}/SRR{srr_num}.fastq.gz ./")
                elif len(srr_num) == 8:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/0{srr_num[-2:]}/SRR{srr_num}/SRR{srr_num}.fastq.gz ./")
                else:
                    print(f"{srr_num}填写错误")
                    continue
def double_seq():
    with open(args.input, "r", encoding="UTF-8") as f:
        for x in f:
            list1 = x.strip().split("/")
            if list1[1]:
                os.system(f"mkdir {list1[1].strip()}")
                srr_num = list1[0].upper().strip("SRR").strip()
                if len(srr_num) == 6:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/SRR{srr_num}/SRR{srr_num}_1.fastq.gz {list1[1].strip()}")
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/SRR{srr_num}/SRR{srr_num}_2.fastq.gz {list1[1].strip()}")
                elif len(srr_num) == 7:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/00{srr_num[-1]}/SRR{srr_num}/SRR{srr_num}_1.fastq.gz {list1[1].strip()}")
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/00{srr_num[-1]}/SRR{srr_num}/SRR{srr_num}_2.fastq.gz {list1[1].strip()}")
                elif len(srr_num) == 8:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/0{srr_num[-2:]}/SRR{srr_num}/SRR{srr_num}_1.fastq.gz {list1[1].strip()}")
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/0{srr_num[-2:]}/SRR{srr_num}/SRR{srr_num}_2.fastq.gz {list1[1].strip()}")
                else:
                    print(f"{srr_num}填写错误")
                    continue
            else:
                srr_num = list1[0].upper().strip("SRR").strip()
                if len(srr_num) == 6:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/SRR{srr_num}/SRR{srr_num}_1.fastq.gz ./")
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/SRR{srr_num}/SRR{srr_num}_2.fastq.gz ./")
                elif len(srr_num) == 7:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/00{srr_num[-1]}/SRR{srr_num}/SRR{srr_num}_1.fastq.gz ./")
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/00{srr_num[-1]}/SRR{srr_num}/SRR{srr_num}_2.fastq.gz ./")
                elif len(srr_num) == 8:
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/0{srr_num[-2:]}/SRR{srr_num}/SRR{srr_num}_1.fastq.gz ./")
                    os.system(
                        f"ascp -v -Q -T -l 500m -P 33001 -k 1 -i {args.key} era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR{srr_num[:3]}/0{srr_num[-2:]}/SRR{srr_num}/SRR{srr_num}_2.fastq.gz ./")
                else:
                    print(f"{srr_num}填写错误")
                    continue

try:
    if args.key:
        if args.type == "1":
            single_seq()
        elif args.type == "2":
            double_seq()
        else:
            print("未输入单端测序还是双端测序")
    else:
        print("未输入密匙文件路径")
except Exception as e:
    print(e)