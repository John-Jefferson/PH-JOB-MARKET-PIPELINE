import pandas as pd
import foundit, jobstreet
from sqlalchemy import create_engine, text
from sqlalchemy import inspect

engine = create_engine("postgresql+psycopg2://johnjefferson:june12006@localhost:5432/jobapplidb")

def sendData(dfName, count):
    df = []
    if(dfName == "jobstreet"):
        df = pd.DataFrame(jobstreet.jobStreetScraper(count))
    else:
        df = pd.DataFrame(foundit.founditScraper(count))
    table_name = f"{dfName}_raw_table"
    temp_table = f"temp_{dfName}_incoming"

    inspector = inspect(engine)
    table_exists = inspector.has_table(table_name, schema="bronze")
    if not table_exists:
        # First time — no existing data to compare against, just insert everything
        new_df = df
    else:
        with engine.begin() as conn:
            df.to_sql(
                name= temp_table,
                schema="bronze",
                con=conn,
                if_exists="replace",
                index=False
            )
            filtered_rows_query = text(f"""            SELECT t.*
                FROM bronze.{temp_table} t
                LEFT JOIN bronze.{table_name} b
                    ON t.link = b.link
                WHERE b.link IS NULL;
            """)
            new_df = pd.read_sql(filtered_rows_query, conn)
            conn.execute(text(f"DROP TABLE IF EXISTS {temp_table};"))
    if new_df.empty:
        print(f"No new rows for {dfName} — all links already exist.")
        return
    
    new_df.to_sql(
        name=table_name,
        schema="bronze",
        con=engine,
        if_exists="append",
        index=False
    )
    if (len(new_df) < count):
        sendData(dfName, (count - len(new_df)))
    print(f"Inserted {len(new_df)} new rows into {table_name}.")

sendData("jobstreet", 10)
sendData("foundit", 10)


"""def sendData(df, dfName):
    df['ID'] = df.index + 1

    jobTitleTable = df[["ID", "title"]].copy()
    skillsTable = df[['ID', 'skills']].copy()
    QualificationsTable = df[['ID', 'qualifications']].copy()
    single_Val_Col_Table = df.drop(columns=["title", 'description', 'skills', 'qualifications']).copy()
    tables = {
        f"{dfName}_raw_job_title": jobTitleTable,
        f"{dfName}_raw_skills": skillsTable,
        f"{dfName}_raw_qualifications": QualificationsTable,
        f"{dfName}_raw_single_val_table": single_Val_Col_Table
    }

    for table_name, table_df in tables.items():
        table_df.to_sql(
            name=table_name,
            schema="bronze",
            con=engine,
            if_exists="append",
            index=False
        )
sendData(jobStreetDF, "jobstreet")
sendData(foundItDF, "foundt")"""