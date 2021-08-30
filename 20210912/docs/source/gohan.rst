ごはんでまなぶ非同期処理
========================

.. drawio-image:: gohan.drawio
   :format: png

- 「米を炊く」と「調理する」は同時にできる
- 「味噌汁をつくる」が終わってから「おかずをつくる」
- 「米を炊く」と「調理する」が両方おわったら「いただきます」

コード例
--------

.. literalinclude:: gohan.py
   :linenos:

出力例
------

.. literalinclude:: gohan.txt