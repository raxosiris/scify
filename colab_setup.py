from google.colab import auth

def colab_setup(gh_name, gh_password, bucket_folder="scify/data/*"):
  """Needs GH details because the REPO is private!"""
  auth.authenticate_user()

  #remove colab folders to sync with GH better
  !rm -r sample_data/
  !git clone https://{gh_name}:{gh_password}@github.com/mkstra/scify.git
  !curl https://sdk.cloud.google.com | bash
  
  #put contents into root
  !mv scify scify_temp
  !mv -v scify_temp/* .
  !rm -r scify_temp

  #get data from bucket
  !gsutil cp -r gs://{bucket_folder} data
