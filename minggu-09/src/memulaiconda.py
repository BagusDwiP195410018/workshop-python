
(base) C:\Users\asus>conda --version
conda 4.12.0

(base) C:\Users\asus>conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\asus\anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
    ------------------------------------------------------------
                                           Total:         729 KB

The following packages will be UPDATED:

  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-package-handli | 729 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(base) C:\Users\asus>conda create --name snowflakes biopython
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\asus\anaconda3\envs\snowflakes

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |   py39h2bbff1b_0         2.1 MB
    ca-certificates-2022.3.29  |       haa95532_0         122 KB
    certifi-2021.10.8          |   py39haa95532_2         152 KB
    numpy-1.21.5               |   py39h7a0a035_1          25 KB
    numpy-base-1.21.5          |   py39hca35cd5_1         4.4 MB
    openssl-1.1.1n             |       h2bbff1b_0         4.8 MB
    python-3.9.12              |       h6244533_0        17.1 MB
    setuptools-61.2.0          |   py39haa95532_0         1.0 MB
    six-1.16.0                 |     pyhd3eb1b0_1          18 KB
    sqlite-3.38.2              |       h2bbff1b_0         807 KB
    tzdata-2022a               |       hda174b7_0         109 KB
    wheel-0.37.1               |     pyhd3eb1b0_0          33 KB
    ------------------------------------------------------------
                                           Total:        30.7 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py39h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  numpy              pkgs/main/win-64::numpy-1.21.5-py39h7a0a035_1
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py39hca35cd5_1
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
setuptools-61.2.0    | 1.0 MB    | ############################################################################ | 100%
wheel-0.37.1         | 33 KB     | ############################################################################ | 100%
certifi-2021.10.8    | 152 KB    | ############################################################################ | 100%
numpy-base-1.21.5    | 4.4 MB    | ############################################################################ | 100%
tzdata-2022a         | 109 KB    | ############################################################################ | 100%
biopython-1.78       | 2.1 MB    | ############################################################################ | 100%
ca-certificates-2022 | 122 KB    | ############################################################################ | 100%
six-1.16.0           | 18 KB     | ############################################################################ | 100%
python-3.9.12        | 17.1 MB   | ############################################################################ | 100%
numpy-1.21.5         | 25 KB     | ############################################################################ | 100%
sqlite-3.38.2        | 807 KB    | ############################################################################ | 100%
openssl-1.1.1n       | 4.8 MB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snowflakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\asus>conda activate snowflakes

(snowflakes) C:\Users\asus>conda info --envs
# conda environments:
#
base                     C:\Users\asus\anaconda3
snowflakes            *  C:\Users\asus\anaconda3\envs\snowflakes


(snowflakes) C:\Users\asus>conda activate

(base) C:\Users\asus>conda info --envs
# conda environments:
#
base                  *  C:\Users\asus\anaconda3
snowflakes               C:\Users\asus\anaconda3\envs\snowflakes


(base) C:\Users\asus>conda create --name snakes python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\asus\anaconda3\envs\snakes

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\asus>conda activate snakes

(snakes) C:\Users\asus>conda info --envs
# conda environments:
#
base                     C:\Users\asus\anaconda3
snakes                *  C:\Users\asus\anaconda3\envs\snakes
snowflakes               C:\Users\asus\anaconda3\envs\snowflakes


(snakes) C:\Users\asus>$
'$' is not recognized as an internal or external command,
operable program or batch file.

(snakes) C:\Users\asus>python --version
Python 3.9.12



(snakes) C:\Users\asus>conda search beautifulsoup4
Loading channels: done
# Name                       Version           Build  Channel
beautifulsoup4                 4.6.0          py27_1  pkgs/main
beautifulsoup4                 4.6.0  py27hc287451_1  pkgs/main
beautifulsoup4                 4.6.0          py35_1  pkgs/main
beautifulsoup4                 4.6.0  py35h61fcdcc_1  pkgs/main
beautifulsoup4                 4.6.0          py36_1  pkgs/main
beautifulsoup4                 4.6.0  py36hd4cc5e8_1  pkgs/main
beautifulsoup4                 4.6.0          py37_1  pkgs/main
beautifulsoup4                 4.6.1          py27_0  pkgs/main
beautifulsoup4                 4.6.1          py35_0  pkgs/main
beautifulsoup4                 4.6.1          py36_0  pkgs/main
beautifulsoup4                 4.6.1          py37_0  pkgs/main
beautifulsoup4                 4.6.3          py27_0  pkgs/main
beautifulsoup4                 4.6.3          py35_0  pkgs/main
beautifulsoup4                 4.6.3          py36_0  pkgs/main
beautifulsoup4                 4.6.3          py37_0  pkgs/main
beautifulsoup4                 4.7.1          py27_1  pkgs/main
beautifulsoup4                 4.7.1          py36_1  pkgs/main
beautifulsoup4                 4.7.1          py37_1  pkgs/main
beautifulsoup4                 4.8.0          py27_0  pkgs/main
beautifulsoup4                 4.8.0          py36_0  pkgs/main
beautifulsoup4                 4.8.0          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py27_0  pkgs/main
beautifulsoup4                 4.8.1          py36_0  pkgs/main
beautifulsoup4                 4.8.1          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py38_0  pkgs/main
beautifulsoup4                 4.8.2          py27_0  pkgs/main
beautifulsoup4                 4.8.2          py36_0  pkgs/main
beautifulsoup4                 4.8.2          py37_0  pkgs/main
beautifulsoup4                 4.8.2          py38_0  pkgs/main
beautifulsoup4                 4.9.0          py36_0  pkgs/main
beautifulsoup4                 4.9.0          py37_0  pkgs/main
beautifulsoup4                 4.9.0          py38_0  pkgs/main
beautifulsoup4                 4.9.1          py36_0  pkgs/main
beautifulsoup4                 4.9.1  py36haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py37_0  pkgs/main
beautifulsoup4                 4.9.1  py37haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py38_0  pkgs/main
beautifulsoup4                 4.9.1  py38haa95532_0  pkgs/main
beautifulsoup4                 4.9.1  py39haa95532_0  pkgs/main
beautifulsoup4                 4.9.3    pyha847dfd_0  pkgs/main
beautifulsoup4                 4.9.3    pyhb0f4dca_0  pkgs/main
beautifulsoup4                4.10.0    pyh06a4308_0  pkgs/main

(snakes) C:\Users\asus>conda install beautifulsoup4
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\asus\anaconda3\envs\snakes

  added / updated specs:
    - beautifulsoup4


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    soupsieve-2.3.1            |     pyhd3eb1b0_0          34 KB
    ------------------------------------------------------------
                                           Total:          34 KB

The following NEW packages will be INSTALLED:

  beautifulsoup4     pkgs/main/noarch::beautifulsoup4-4.10.0-pyh06a4308_0
  soupsieve          pkgs/main/noarch::soupsieve-2.3.1-pyhd3eb1b0_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
soupsieve-2.3.1      | 34 KB     | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(snakes) C:\Users\asus>conda list
# packages in environment at C:\Users\asus\anaconda3\envs\snakes:
#
# Name                    Version                   Build  Channel
beautifulsoup4            4.10.0             pyh06a4308_0
ca-certificates           2022.3.29            haa95532_0
certifi                   2021.10.8        py39haa95532_2
openssl                   1.1.1n               h2bbff1b_0
pip                       21.2.4           py39haa95532_0
python                    3.9.12               h6244533_0
setuptools                61.2.0           py39haa95532_0
soupsieve                 2.3.1              pyhd3eb1b0_0
sqlite                    3.38.2               h2bbff1b_0
tzdata                    2022a                hda174b7_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wheel                     0.37.1             pyhd3eb1b0_0
wincertstore              0.2              py39haa95532_2




(snakes) C:\Users\asus>