# hashMap

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day0728 {
    /**
     * <pre>
     * 코드값을 가져온다.
     * 코드별 key를 분리하여 반환.(return 예시 참조)
     *
     * @param param
     *   - dc_reqCode : 코드 조회 파라메터
     *     - GRP_CD : 조회할 코드값. ,로 구분.
     * 예시 ) {"dc_reqCode":{ "GRP_CD":"101,02" }}
     * @return
     * {
     *     "dc_code101": [
     *        {
     *           "GRP_CD": "101",
     *           "CODE_CD": "M",
     *           "CODE_NM": "남"
     *        },
     *        {
     *           "GRP_CD": "101",
     *           "CODE_CD": "F",
     *           "CODE_NM": "여"
     *        }
     *     ],
     *     "dc_code02": [
     *        {
     *           "GRP_CD": "02",
     *           "CODE_CD": "02",
     *           "CODE_NM": "이사"
     *        },
     *        {
     *           "GRP_CD": "02",
     *           "CODE_CD": "07",
     *           "CODE_NM": "사원"
     *        }
     *     ],
     *     "msgCode": "S",
     *     "msg": "공통코드 조회가 완료되었습니다."
     * }
     * @throws Exception
     * </pre>
     */

    @RequestMapping(value = "/training/test.dio")
    public Map getCodeList(@RequestBody Map param) throws Exception {

        param = {"dc_reqCode":{ "GRP_CD":"101,02" }};

        Map resObj = new HashMap();
        Map commonCode;
        String GRP_CD;
        String dataIdPrefix = "dc_code";
        String[] selectCodeList;

        try {
            commonCode = (Map) param.get("dc_reqCode");
            GRP_CD = (String) commonCode.get("GRP_CD");

            if(GRP_CD != null) {
                GRP_CD = GRP_CD.replaceAll(" ", ""); // 공백 제거
            }

            selectCodeList = GRP_CD.split(",");
            commonCode.put("CODE", selectCodeList); // ["101", "02"]

            List codeList = new ArrayList<>();

            HashMap<String, String> info1 = new HashMap<>() {{
                put("GRP_CD", "02");
                put("CODE_CD", "02");
                put("CODE_NM", "이사");
            }};

            HashMap<String, String> info2 = new HashMap<>() {{
                put("GRP_CD", "02");
                put("CODE_CD", "07");
                put("CODE_NM", "사원");
            }};

            codeList.add(info1);
            codeList.add(info2);

            //여러건의 code를 가져올 때 code별로 객체 생성
            if(selectCodeList.length > 1){
                int size = codeList.size();
                String preCode = "";
                List codeGroupList = null;
                for (int i = 0; i < size; i++ ) {
                    Map codeMap = (Map)codeList.remove(0); // 맨 앞부터 가져옴
                    String grp_cd = (String)codeMap.get("GRP_CD"); // "02"
                    if ( !preCode.equals(grp_cd)) { // 다른 코드라면
                        if ( codeGroupList != null ){ // 그룹리스트가 있다면 추가
                            resObj.put(dataIdPrefix + preCode, codeGroupList);
                        }
                        preCode = grp_cd; // 새 코드세트 생성
                        codeGroupList = new ArrayList(); 
                        codeGroupList.add(codeMap);
                    } else {
                        codeGroupList.add(codeMap); // 같은 코드라면 리스트에 추가
                    }

                    if ( i == size-1 ){
                        resObj.put(dataIdPrefix + preCode, codeGroupList);
                    }
                }

            }else {
                resObj.put(dataIdPrefix + selectCodeList[0], codeList);
            }


            resObj.put("msg", "공통코드 조회가 완료되었습니다.");
            resObj.put("msgCode", "S");

        } catch (Exception ex) {
            ex.printStackTrace();
            resObj = EduUtils.setErrorMessage(resObj);
        }

        return resObj;
    }
}

```

