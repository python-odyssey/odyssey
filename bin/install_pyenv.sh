curl https://pyenv.run | bash

echo "" >> ~/.profile
echo "# Automatically setup pyenv" >> ~/.profile
echo "export PATH=\"/root/.pyenv/bin:\$PATH\"" >> ~/.profile
echo "eval \"\$(pyenv init -)\"" >> ~/.profile
echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.profile

. ~/.profile
