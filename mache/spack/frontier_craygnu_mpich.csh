source /opt/cray/pe/lmod/lmod/init/csh

module reset

module load \
    PrgEnv-gnu \
    cpe/24.11 \
    libunwind/1.8.1 \
    subversion/1.14.2 \
    git/2.45.1 \
    cmake/3.27.9

module rm \
    darshan-runtime &> /dev/null

{% if e3sm_hdf5_netcdf %}
module load \
    cray-hdf5-parallel/1.14.3.3 \
    cray-netcdf-hdf5parallel/4.9.0.15 \
    cray-parallel-netcdf/1.12.3.15
{% endif %}

setenv HDF5_ROOT ""
setenv MPICH_GPU_SUPPORT_ENABLED "0"
setenv MPICH_VERSION_DISPLAY "1"
setenv MPICH_OFI_CXI_COUNTER_REPORT "2"
setenv LD_LIBRARY_PATH "${CRAY_LD_LIBRARY_PATH}:${LD_LIBRARY_PATH}"
setenv SKIP_BLAS "True"
setenv GPUS_PER_NODE " "
setenv NTASKS_PER_GPU " "
setenv GPU_BIND_ARGS " "
setenv PKG_CONFIG_PATH "/lustre/orion/cli115/world-shared/frontier/3rdparty/protobuf/21.6/gcc-native-13.2/lib/pkgconfig:${PKG_CONFIG_PATH}"

{% if e3sm_hdf5_netcdf %}
setenv NETCDF_PATH "${NETCDF_DIR}"
setenv NETCDF_C_PATH "${NETCDF_DIR}"
setenv NETCDF_FORTRAN_PATH "${NETCDF_DIR}"
setenv PNETCDF_PATH "${PNETCDF_DIR}"
{% endif %}
