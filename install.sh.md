# create conda env
conda create -n vnpy python=3.13
conda activate vnpy

# change mirrors
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# install ta-lib
mkdir tmp
cd tmp
wget https://pip.vnpy.com/colletion/ta-lib-0.6.4-src.tar.gz
tar -xf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4
./configure --prefix=/usr/local
make -j8
sudo make install
cd ../
rm -rf tmp

pip install ta-lib==0.6.4


# install other modules
pip install .

pip install vnpy_sqlite vnpy_ctastrategy vnpy_ctabacktester vnpy_chartwizard vnpy_scripttrader vnpy_datamanager vnpy_datarecorder vnpy_ctp vnpy_tushare


# 运行
python examples/veighna_trader/run.py

# 报错
报错：
ImportError: /tmp/pip-install-6qztqklm/vnpy-ctp_d3fcb7c989b74290bfa252416562e58a/vnpy_ctp/api/libthostmduserapi_se.so: cannot open shared object file: No such file or directory
解决：
pip uninstall vnpy_ctp
git clone git@github.com:vnpy/vnpy_ctp.git
conda activate vnpy
pip install .

报错：
ImportError: /home/lutao/miniconda3/envs/vnpy/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by /home/lutao/miniconda3/envs/vnpy/lib/python3.13/site-packages/vnpy_ctp/api/vnctpmd.cpython-313-x86_64-linux-gnu.so)
解决：
conda install -c conda-forge libstdcxx-ng=13.3.0