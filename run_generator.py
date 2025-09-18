#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 HDGRACE BAS 29.3.1 XML Generator - 간편 실행 스크립트
상업 배포용 7170개 기능 완전 통합 XML 생성
"""

import sys
import os
from datetime import datetime

def main():
    print("🚀 HDGRACE Enterprise BAS 29.3.1 XML Generator")
    print("=" * 60)
    print("📌 7170개 기능 완전 통합 상업 배포용 XML 생성기")
    print("🎯 BAS 29.3.1 규격 100% 호환")
    print("🏢 실전 상업 배포용 - 테스트 금지, 예시 금지")
    print("=" * 60)
    print()
    
    # 메인 생성기 실행
    try:
        from hdgrace_bas_xml_generator import HDGRACEXMLGenerator, HDGRACEEnterpriseConfig
        
        print("🔧 생성기 초기화 중...")
        config = HDGRACEEnterpriseConfig()
        generator = HDGRACEXMLGenerator(config)
        
        print("⚡ XML 생성 시작...")
        start_time = datetime.now()
        
        filepath = generator.run()
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print()
        print("🎉 생성 완료!")
        print(f"📁 파일 경로: {filepath}")
        print(f"📊 파일 크기: {os.path.getsize(filepath) / (1024*1024):.2f} MB")
        print(f"⏰ 소요 시간: {duration:.2f}초")
        print()
        print("✅ HDGRACE Enterprise BAS 29.3.1 XML 생성이 성공적으로 완료되었습니다!")
        print("🎯 생성된 XML 파일을 BrowserAutomationStudio 29.3.1에서 열어서 사용하세요.")
        
        return 0
        
    except ImportError as e:
        print(f"❌ 모듈 가져오기 실패: {e}")
        print("💡 다음 명령으로 의존성을 설치하세요:")
        print("   pip install -r requirements.txt")
        return 1
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())