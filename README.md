# uniprot2IBS
 convert Uniprot metadata xml to IBS project xml for visualization

## Requirements

- Python
- pandas
- jinja2

## Useage

### clone this project
```shell
git clone https://github.com/Stella3055/uniprot2IBS.git
cd uniprot2IBS
```
or simply download the project .zip archive and uncompress

### Downloading .xml metadata from Uniprot
![fig1](https://github.com/Stella3055/uniprot2IBS/raw/master/assert/fig1.png)

### Extract structure info
```shell
python ./uniprot2IBS.py parse ./ESR1.xml
```
then a ESR1.xml.info.tsv file will be generated

### Trim the .tsv file, only keep interested structures
xml metadata file contains many structure info about a protein, if all of them are kept the figure will be crowded. Trim the file by rows and only keep interested rows.
```
# generated
feature_name	description	Start_Position	End_Position	Loci_Position
chain	Estrogen receptor	1	595	NA
domain	NR LBD	311	547	NA
DNA-binding region	Nuclear receptor	185	250	NA
zinc finger region	NR C4-type	185	205	NA
zinc finger region	NR C4-type	221	245	NA
region of interest	Modulating (transactivation AF-1); mediates interaction with MACROD1	1	184	NA
region of interest	Interaction with DDX5; self-association	35	174	NA
region of interest	Required for interaction with NCOA1	35	47	NA
region of interest	Mediates interaction with DNTTIP2	185	310	NA
region of interest	Hinge	251	310	NA
region of interest	Interaction with AKAP13	262	595	NA
region of interest	Self-association	264	595	NA
region of interest	Transactivation AF-2	311	595	NA
modified residue	Phosphoserine; by CDK2	NA	NA	104
modified residue	Phosphoserine; by CDK2	NA	NA	106
modified residue	Phosphoserine	NA	NA	118
modified residue	Phosphoserine; by CK2	NA	NA	167
modified residue	Asymmetric dimethylarginine; by PRMT1	NA	NA	260
modified residue	Phosphotyrosine; by Tyr-kinases	NA	NA	537
lipid moiety-binding region	S-palmitoyl cysteine	NA	NA	447
glycosylation site	O-linked (GlcNAc) serine	NA	NA	10
splice variant	In isoform 3 and isoform 4.	1	173	NA
splice variant	In isoform 2.	255	366	NA
splice variant	In isoform 4.	458	595	NA
sequence variant	In a breast cancer sample; somatic mutation; dbSNP:rs139960913.	NA	NA	6
sequence variant	In dbSNP:rs9340773.	NA	NA	77
sequence variant	In dbSNP:rs149308960.	NA	NA	160
sequence variant	In a breast cancer sample; somatic mutation.	NA	NA	264
sequence variant	In ESTRR; results in highly reduced activity; dbSNP:rs397509428.	NA	NA	375
sequence variant	In ESTRR; highly decreased estrogen receptor activity; dbSNP:rs1131692059.	NA	NA	394
sequence variant	Destabilizes the receptor and decreases its affinity for estradiol at 25 degrees Celsius, but not at 4 degrees Celsius.	NA	NA	400
sequence variant	In a 80 kDa form found in a breast cancer line; contains an in-frame duplication of exons 6 and 7.	NA	NA	411
mutagenesis site	Impairs AF-1 transactivation.	NA	NA	39
mutagenesis site	Impairs AF-1 transactivation.	NA	NA	43
mutagenesis site	Loss of cyclin A-dependent induction of transcriptional activation.	NA	NA	104
mutagenesis site	Loss of cyclin A-dependent induction of transcriptional activation.	NA	NA	106
mutagenesis site	Decreases phosphorylation and transactivation activity. Abolishes AF-1 transactivation. Insensitive to PPP5C inhibition of transactivation activity.	NA	NA	118
mutagenesis site	Enhances transactivation activity. Enhances interaction with DDX5. Insensitive to PPP5C inhibition of transactivation activity.	NA	NA	118
mutagenesis site	Loss of methylation.	NA	NA	260
mutagenesis site	Has higher transcriptional activity in the absence of wild type ER. Inhibits transcriptional activity when coexpressed with the wild type receptor.	NA	NA	364
mutagenesis site	Loss of transmembrane localization, no effect on peripheral membrane localization. Impairs activation of estrogen-induced activation of NOS3 and production of nitric oxide. No effect on binding to ERES.	NA	NA	386
mutagenesis site	Loss of hormone binding capacity and temperature-sensitive loss in DNA-binding.	NA	NA	447
mutagenesis site	Abolishes interaction with NCOA1, NCOA2 and NCOA3.	NA	NA	539
sequence conflict	In Ref. 5; CAE45969.	NA	NA	452
turn	NA	186	188	NA
strand	NA	189	191	NA
strand	NA	194	196	NA
strand	NA	199	201	NA
helix	NA	203	213	NA
strand	NA	222	225	NA
turn	NA	231	236	NA
helix	NA	238	248	NA
helix	NA	288	291	NA
helix	NA	302	304	NA
helix	NA	307	309	NA
helix	NA	312	322	NA
strand	NA	330	332	NA
strand	NA	334	336	NA
helix	NA	339	361	NA
helix	NA	367	369	NA
helix	NA	372	394	NA
turn	NA	395	397	NA
strand	NA	402	405	NA
strand	NA	408	410	NA
helix	NA	412	415	NA
strand	NA	418	420	NA
helix	NA	421	438	NA
helix	NA	442	455	NA
helix	NA	458	460	NA
turn	NA	464	466	NA
helix	NA	467	469	NA
helix	NA	473	492	NA
helix	NA	497	530	NA
strand	NA	531	533	NA
helix	NA	538	545	NA
helix	NA	547	549	NA
helix	NA	588	590	NA
```
and then
```
# we only kept informations about the chain(necessary), 2 domains and 2 mutation sites
feature_name	description	Start_Position	End_Position	Loci_Position
chain	Estrogen receptor	1	595	NA
domain	NR LBD	311	547	NA
DNA-binding region	Nuclear receptor	185	250	NA
mutagenesis site	Impairs AF-1 transactivation.	NA	NA	39
mutagenesis site	Impairs AF-1 transactivation.	NA	NA	43
```

### construct IBS project file
```shell
python ./uniprot2IBS.py construct ./ESR1.xml.info.tsv
```
ESR1.xmlinfo.tsv.ibs.xml will be generated

### Use IBS to open and modify the generated figure

[IBS download](http://ibs.biocuckoo.org/download.php)

Open IBS-->Protein Mode-->File-->Open Project-->select ESR1.xml.info.tsv.ibs.xml

![fig2](https://github.com/Stella3055/uniprot2IBS/raw/master/assert/fig2.png)

then edit it

![fig3](https://github.com/Stella3055/uniprot2IBS/raw/master/assert/fig3.png)