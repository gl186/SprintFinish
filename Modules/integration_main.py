import module2_variantvalidator
import module3_VV_LOVD_code_only

variant_description = module2_variantvalidator.test_return_hgvs()
genome_build = "hg19"
select_transcripts = "mane_select"

dict_possible_variants = module3_VV_LOVD_code_only.get(genome_build,variant_description,select_transcripts)
print(dict_possible_variants)