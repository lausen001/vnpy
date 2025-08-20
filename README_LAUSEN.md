# vnpy

vnpy 教程。

## conda环境安装

### 创建conda环境

```
conda create -n vnpy python=3.13
conda activate vnpy
```

### 换源加速

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 安装 ta-lib

```
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
```

### 安装其他依赖

```
pip install .

pip install vnpy_sqlite vnpy_ctastrategy vnpy_ctabacktester vnpy_chartwizard vnpy_scripttrader vnpy_datamanager vnpy_datarecorder vnpy_ctp vnpy_tushare vnpy_spreadtrading
```

### 运行

```
python examples/veighna_trader/run.py
```


## 报错


报错：ImportError: /tmp/pip-install-6qztqklm/vnpy-ctp_d3fcb7c989b74290bfa252416562e58a/vnpy_ctp/api/libthostmduserapi_se.so: cannot open shared object file: No such file or directory

解决：
```
pip uninstall vnpy_ctp
git clone git@github.com:vnpy/vnpy_ctp.git
conda activate vnpy
pip install .
```

报错：
ImportError: /home/lutao/miniconda3/envs/vnpy/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by /home/lutao/miniconda3/envs/vnpy/lib/python3.13/site-packages/vnpy_ctp/api/vnctpmd.cpython-313-x86_64-linux-gnu.so)

解决：
```
conda install -c conda-forge libstdcxx-ng=13.3.0
```

## veighna trader操作

前置操作

1. 在 https://www.simnow.com.cn/ 注册CTP仿真账号，在 https://www.simnow.com.cn/product.action 获取服务器地址。
2. connect CTP。


打开run.py注释的其他功能，提示缺少一些模块

```
pip install vnpy_spreadtrading vnpy_paperaccount vnpy_algotrading vnpy_optionmaster vnpy_portfoliostrategy vnpy_rpcservice vnpy_excelrtd vnpy_riskmanager vnpy_webtrader vnpy_portfoliomanager
```

界面切换成中文，修改vnpy/trader/locale/__init__.py，加上：languages=["zh_CN"]

```
translations: gettext.GNUTranslations | gettext.NullTranslations = gettext.translation("vnpy", localedir=localedir, languages=["zh_CN"], fallback=True)
```