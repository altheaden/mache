setenv http_proxy http://proxyout.lanl.gov:8080/
setenv https_proxy http://proxyout.lanl.gov:8080/
setenv ftp_proxy http://proxyout.lanl.gov:8080
setenv HTTP_PROXY http://proxyout.lanl.gov:8080
setenv HTTPS_PROXY http://proxyout.lanl.gov:8080
setenv FTP_PROXY http://proxyout.lanl.gov:8080

source /usr/share/lmod/8.3.1/init/csh

module rm PrgEnv-gnu
module rm PrgEnv-nvidia
module rm PrgEnv-cray
module rm PrgEnv-aocc
module rm craype-accel-nvidia80
module rm craype-accel-host

module load PrgEnv-gnu/8.3.3
module load gcc/12.1.0
module load craype-accel-host
{% if e3sm_lapack %}
module load cray-libsci
{% endif %}
module load craype
module load cray-mpich/8.1.21
{% if e3sm_hdf5_netcdf %}
module rm cray-hdf5-parallel
module rm cray-netcdf-hdf5parallel
module rm cray-parallel-netcdf
module load cray-hdf5-parallel/1.12.2.1
module load cray-netcdf-hdf5parallel/4.9.0.1
module load cray-parallel-netcdf/1.12.3.1
{% endif %}
module load cmake/3.20.3

setenv NETCDF_C_PATH $(dirname $(dirname $(which nc-config)))
setenv NETCDF_FORTRAN_PATH $(dirname $(dirname $(which nf-config)))
setenv PNETCDF_PATH $(dirname $(dirname $(which pnetcdf_version)))
setenv MPICH_ENV_DISPLAY 1
setenv MPICH_VERSION_DISPLAY 1
setenv OMP_STACKSIZE 128M
setenv OMP_PROC_BIND spread
setenv OMP_PLACES threads
setenv HDF5_USE_FILE_LOCKING FALSE
setenv PERL5LIB /usr/projects/climate/SHARED_CLIMATE/software/chicoma-cpu/perl5-only-switch/lib/perl5