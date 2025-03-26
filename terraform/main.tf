terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project     = "inspiring-code-453522-m5"
  region      = "us-central1"
}

resource "google_storage_bucket" "data-lake-bucket" {
  name          = "buc-inspiring-453522_m5"  # Make it globally unique
  location      = "US"
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 60  # days
    }
  }
}
resource "google_bigquery_dataset" "bigquerydataset" {
  dataset_id = "soomro_zoomcamp_DS"
  project    = "inspiring-code-453522-m5"
  location   = "US"
}
