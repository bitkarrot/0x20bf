##### [make](https://www.gnu.org/software/make/)
 	make  [COMMAND]
 	
 	      help
 	      init                initialize requirements
 	
 	      venv                create python3 virtual environment
 	
 	make  venv && . venv/bin/activate
 	
 	      venv-clean	  rm -rf venv
 	      venv-test           python3 ./tests/test.py
 	      venv-test-gnupg	  test gnupg in venv
 	      test-gnupg          python3 ./tests/.../setup.py
 	                                  ./tests/.../test_gnupg.py
 	
 	      build               python3 setup.py build
 	      install             python3 -m pip install -e .
 	      report              environment args
 	      initialize          run scripts/initialize
 	      requirements        pip install --user -r requirements.txt
 	      vendors             make seeder legit gogs
 	      seeder              make -C vendor/seeder
 	      legit               pushd vendors/legit && cargo build --release
 	      gogs                make -C vendors/gogs
 	
 	      depends             build depends
 	      depends-gnupg-test  test 0x20bf/depends/gnupg library
 	      depends-gnupg       install python gnupg on host
 	      depends-p2p         install python p2p-network
 	      depends-fastapi     install python fastapi
 	      pre-commit          pre-commit run -a
 	
 	      docs                build docs from sources/*.md
 	
 	      clean               venv-clean
 	                          rm -rf build dist rokeys
