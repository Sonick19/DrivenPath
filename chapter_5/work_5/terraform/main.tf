provider "aws" {
	region = var.region
}

locals {
  glue_scripts = {
    "dim_address" = "dim_address.py.tmpl"
    "dim_date" = "dim_date.py.tmpl"
    "dim_finance" = "dim_finance.py.tmpl"
    "dim_person" = "dim_person.py.tmpl"
	"fact_network_usage" = "fact_network_usage.py.tmpl"
  }
}

resource "local_file" "rendered_scripts" {
  for_each = local.glue_scripts

  content  = templatefile("${path.module}/tasks/${each.value}", {
    bucket_name = var.bucket_name
  })

  filename = "${path.module}/tasks/${each.key}.py"
}
